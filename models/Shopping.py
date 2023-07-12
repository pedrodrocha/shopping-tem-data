from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.shopping_address import ShoppingAddress
    from models.shopping_opening_hour import ShoppingOpeningHour
    from models.shopping_phone import ShoppingPhone
    from models.store import Store

class Shopping(TimestampMixin, Base):
    __tablename__ = "shoppings"

    name: Mapped[str] = mapped_column(String(255))
    site_url: Mapped[str] = mapped_column(String(255))

    shopping_phones: Mapped[list[ShoppingPhone]] = relationship(
        "ShoppingPhone",
        back_populates="shopping",
    )

    shopping_address: Mapped[ShoppingAddress] = relationship(
        "ShoppingAddress",
        back_populates="shopping",
    )

    shopping_opening_hours: Mapped[list[ShoppingOpeningHour]] = relationship(
        "ShoppingOpeningHour",
        back_populates="shopping",
    )

    stores: Mapped[list[Store]] = relationship(
        "Store",
        back_populates="shopping",
    )

