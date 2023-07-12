from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.Sector import Sector
    from models.Brand import Brand

class Subsector(TimestampMixin, Base):
    __tablename__ = "subsectors"

    sector_id: Mapped[int] = mapped_column(ForeignKey("sectors.id"))
    subsector: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(255))

    sector: Mapped[Sector] = relationship(
        "Sector",
        back_populates="subsectors",
    )

    brands: Mapped[list[Brand]] = relationship(
        'Brand',
        secondary="subsectors_brands",
        back_populates="subsectors"
    )
