from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from fastapi import BackgroundTasks

from app.services.email_service import (
    send_order_email
)
from app.models.customer import Customer
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem

from app.schemas.order import (
    OrderCreate,
    OrderResponse
)

router = APIRouter(
    prefix="/api/v1/orders",
    tags=["Orders"]
)

from fastapi import BackgroundTasks

@router.post("/")
def create_order(
    order: OrderCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    customer = db.query(Customer).filter(
        Customer.id == order.customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    total = 0

    db_order = Order(
        customer_id=order.customer_id
    )

    db.add(db_order)
    db.flush()

    for item in order.items:

        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product {item.product_id} not found"
            )

        if not product.is_active:
            raise HTTPException(
                status_code=400,
                detail=f"{product.name} inactive"
            )

        if item.quantity > product.stock:
            raise HTTPException(
                status_code=400,
                detail=f"Not enough stock for {product.name}"
            )

        product.stock -= item.quantity

        item_total = (
            product.price * item.quantity
        )

        total += item_total

        order_item = OrderItem(
            order_id=db_order.id,
            product_id=product.id,
            quantity=item.quantity,
            price=product.price
        )

        db.add(order_item)

    db_order.total_amount = total

    db.commit()
    background_tasks.add_task(
    send_order_email,
    customer.email
)

    db.refresh(db_order)

    return db_order

@router.get(
    "/",
    response_model=list[OrderResponse]
)


@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@router.put("/{order_id}/cancel")
def cancel_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    if order.status == "Delivered":
        raise HTTPException(
            status_code=400,
            detail="Delivered orders cannot be cancelled"
        )

    order.status = "Cancelled"

    db.commit()

    return {
        "message": "Order cancelled"
    }


@router.get("/")
def get_orders(
    page: int = 1,
    limit: int = 10,
    status: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(Order)

    if status:
        query = query.filter(
            Order.status == status
        )

    total = query.count()

    orders = (
        query.offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    return {
        "total_records": total,
        "current_page": page,
        "data": orders
    }

