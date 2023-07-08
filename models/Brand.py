from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base, TimestampMixin

class Brand(TimestampMixin, Base):
    __tablename__="brands"

    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(255))
    site_url: Mapped[str | None] = mapped_column(String(255))