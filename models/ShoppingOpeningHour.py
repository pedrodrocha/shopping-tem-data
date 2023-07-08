from __future__ import annotations

from datetime import time
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.Shopping import Shopping

class WeekDays(Enum):
    sunday=1
    monday=2
    tuesday=3
    wednesday=4
    thursday=5
    friday=6
    saturday=7

class ShoppingOpeningHour(TimestampMixin, Base):
    __tablename__ = "shopping_opening_hours"

    shopping_id: Mapped[int] = mapped_column(ForeignKey("shoppings.id"))
    week_day: Mapped[WeekDays]
    opening_hour: Mapped[time]
    closing_hour: Mapped[time]


    shopping: Mapped[Shopping] = relationship(
        "Shopping",
        back_populates="shopping_opening_hours",
    )
