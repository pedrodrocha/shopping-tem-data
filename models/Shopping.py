
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin
from models.ShoppingPhone import ShoppingPhone

from typing import List


class Shopping(TimestampMixin, Base):
    __tablename__ = "shoppings"

    name: Mapped[str] = mapped_column(String(255))
    site_url: Mapped[str] = mapped_column(String(255))

    shopping_phones: Mapped[List["ShoppingPhone"]] = relationship(back_populates="shopping_phones")
