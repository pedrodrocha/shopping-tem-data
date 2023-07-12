from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.shopping import Shopping

class ShoppingPhone(TimestampMixin, Base):
    __tablename__ = "shopping_phones"

    shopping_id: Mapped[int] = mapped_column(ForeignKey("shoppings.id"))
    phone: Mapped[int]

    shopping: Mapped[Shopping] = relationship(
        "Shopping",
        back_populates="shopping_phones",
    )
