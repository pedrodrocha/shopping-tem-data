from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.ShoppingAddress import ShoppingAddress
    from models.ShoppingPhone import ShoppingPhone

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
