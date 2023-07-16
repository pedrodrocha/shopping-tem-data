from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.shopping_address import ShoppingAddress
    from models.state import State

class City(TimestampMixin, Base):
    __tablename__ = "cities"

    state_id: Mapped[int] = mapped_column(ForeignKey("states.id"))
    code: Mapped[int]
    city: Mapped[str] = mapped_column(String(255), nullable=False)

    state: Mapped[State] = relationship(
        "State",
        back_populates="cities",
    )

    shopping_address: Mapped[list[ShoppingAddress]] = relationship(
        "ShoppingAddress",
        back_populates="city",
    )

