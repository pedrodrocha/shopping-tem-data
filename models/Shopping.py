from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.Base import Base


class Shopping(Base):
    __tablename__ = "shoppings"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    site_url: Mapped[str] = mapped_column(String(255))
    updated_at: Mapped[datetime | None]
    created_at: Mapped[datetime | None]
