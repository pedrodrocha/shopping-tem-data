from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.store import Store


class StorePhone(TimestampMixin, Base):
    __tablename__ = "store_phones"

    store_id: Mapped[int] = mapped_column(ForeignKey("stores.id"))
    phone: Mapped[int]

    store: Mapped[Store] = relationship(
        "Store",
        back_populates="store_phones",
    )

