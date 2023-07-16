from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.city import City
    from models.shopping import Shopping
    from models.state import State


class ShoppingAddress(TimestampMixin, Base):
    __tablename__ = "shopping_addresses"

    shopping_id: Mapped[int] = mapped_column(ForeignKey("shoppings.id"))
    address_line_1: Mapped[str] = mapped_column(String(255), nullable=True)
    address_line_2: Mapped[str | None] = mapped_column(String(255), nullable=True)
    state_id: Mapped[int] = mapped_column(ForeignKey("states.id"))
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    postal_code: Mapped[int] = mapped_column(Integer)


    shopping: Mapped[Shopping] = relationship(
        "Shopping",
        back_populates="shopping_address",
    )
    
    state: Mapped[State] = relationship(
        "State",
        back_populates="shopping_address",
    )

    city: Mapped[City] = relationship(
        "City",
        back_populates="shopping_address",
    )
