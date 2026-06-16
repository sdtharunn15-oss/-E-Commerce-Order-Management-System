from pydantic import BaseModel


class ShipmentCreate(BaseModel):
    order_id: int
    tracking_number: str


class ShipmentUpdate(BaseModel):
    shipment_status: str


class ShipmentResponse(BaseModel):
    id: int
    order_id: int
    tracking_number: str
    shipment_status: str

    class Config:
        from_attributes = True

