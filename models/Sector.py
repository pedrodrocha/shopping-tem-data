from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.Brand import Brand
    from models.Subsector import Subsector

class Sector(TimestampMixin, Base):
    __tablename__ = "sectors"

    sector: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(255))

    subsectors: Mapped[list[Subsector]] = relationship(
        "Subsector",
        back_populates="sector",
    )

    brands: Mapped[list[Brand]] = relationship(
        "Brand",
        secondary="sectors_brands",
        back_populates="sectors",
    )
