from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.Shopping import Shopping
    from models.Brand import Brand

class Store(TimestampMixin, Base):
    __tablename__="stores"

    
    shopping_id: Mapped[int] = mapped_column(ForeignKey("shoppings.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))
    location: Mapped[str | None] = mapped_column(String(255))

    shopping: Mapped[Shopping] = relationship(
        "Shopping",
        back_populates="stores",
    )

    brand: Mapped[Brand] = relationship(
        'Brand',
        back_populates="stores"
    )