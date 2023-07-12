from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin

if TYPE_CHECKING:
    from models.Sector import Sector
    from models.Subsector import Subsector
    from models.Store import Store

class Brand(TimestampMixin, Base):
    __tablename__="brands"

    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(255))
    site_url: Mapped[str | None] = mapped_column(String(255))

    stores: Mapped[list[Store]] = relationship(
        "Store",
        back_populates="brand",
    )

    sectors: Mapped[list[Sector]] = relationship(
        "Sector",
        secondary="sectors_brands",
        back_populates="brands",
    )

    subsectors: Mapped[list[Subsector]] = relationship(
        'Subsector',
        secondary="subsectors_brands",
        back_populates="brands"
    )
