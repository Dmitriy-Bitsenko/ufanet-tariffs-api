# from typing import Annotated

from sqlmodel import Field, SQLModel


from datetime import datetime, timezone

class TariffBase(SQLModel):
    name: str = Field(index=True)
    price: float 
    city: str
    speed_mbps: int 
    description: str 
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    
class Tariff(TariffBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class TariffRead(TariffBase):
    id: int

