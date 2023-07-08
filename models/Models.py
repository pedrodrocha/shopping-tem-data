

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin
from typing import List


class Shopping(TimestampMixin, Base):
    __tablename__ = "shoppings"

    name: Mapped[str] = mapped_column(String(255))
    site_url: Mapped[str] = mapped_column(String(255))

    shopping_phones: Mapped[List["ShoppingPhone"]] = relationship(back_populates="shopping")

class ShoppingPhone(TimestampMixin, Base):
    __tablename__ = "shopping_phones"

    shopping_id: Mapped[int] = mapped_column(ForeignKey("shoppings.id"))
    phone: Mapped[int]

    shopping: Mapped["Shopping"] = relationship(back_populates="shopping_phones")
