from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.Base import Base, TimestampMixin


class SubsectorBrand(TimestampMixin, Base):
    __tablename__ = "subsectors_brands"

    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))
    subsector_id: Mapped[int] = mapped_column(ForeignKey("subsectors.id"))

