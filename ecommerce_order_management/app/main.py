from fastapi import FastAPI

from app.database import Base, engine

import app.models.user
import app.models.customer
import app.models.product
import app.models.order
import app.models.order_item

from app.routes import auth
from app.routes import customers
from app.routes import products
from app.routes import orders
import app.models.shipment
from app.routes import shipments

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce Order Management System"
)

app.include_router(auth.router)
app.include_router(customers.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(shipments.router)