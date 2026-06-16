from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.order import Order
from app.models.shipment import Shipment

from app.schemas.shipment import (
    ShipmentCreate,
    ShipmentUpdate,
    ShipmentResponse
)

router = APIRouter(
    prefix="/api/v1/shipments",
    tags=["Shipments"]
)


@router.post("/")
def create_shipment(
    shipment: ShipmentCreate,
    db: Session = Depends(get_db)
):
    return shipment

@router.get("/{shipment_id}")
def get_shipment():
    pass


@router.put("/{shipment_id}")
def update_shipment():
    pass


@router.get("/")
def get_shipments(
    page: int = 1,
    limit: int = 10,
    status: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(Shipment)

    if status:
        query = query.filter(
            Shipment.shipment_status == status
        )

    total = query.count()

    shipments = (
        query.offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    return {
        "total_records": total,
        "current_page": page,
        "data": shipments
    }