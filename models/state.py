from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.city import City
    from models.shopping_address import ShoppingAddress

class State(TimestampMixin, Base):
    __tablename__ = "states"

    code: Mapped[int]
    abbr: Mapped[str] = mapped_column(String(255), nullable=False)
    state: Mapped[str] = mapped_column(String(255), nullable=False)

    cities: Mapped[list[City]] = relationship(
        "City",
        back_populates="state",
    )

    shopping_address: Mapped[list[ShoppingAddress]] = relationship(
        "ShoppingAddress",
        back_populates="state",
    )
