from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, TimestampMixin


class SectorBrand(TimestampMixin, Base):
    __tablename__ = "sectors_brands"

    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))
    sector_id: Mapped[int] = mapped_column(ForeignKey("sectors.id"))

