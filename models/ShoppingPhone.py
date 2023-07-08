
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin
from models.Shopping import Shopping


class ShoppingPhone(TimestampMixin, Base):
    __tablename__ = "shopping_phones"

    shopping_id: Mapped[int] = mapped_column(ForeignKey("shoppings.id"))
    phone: Mapped[int]


    shopping: Mapped["Shopping"] = relationship(back_populates='shoppings')
