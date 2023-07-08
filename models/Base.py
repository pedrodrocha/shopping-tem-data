from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    """base sqalalchemy model"""
    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    })

    id: Mapped[int] = mapped_column(primary_key=True)

class TimestampMixin:
    """define timestamp columns for models"""
    updated_at: Mapped[datetime | None] = mapped_column(
        default=datetime.now,
        onupdate=datetime.now,
    )
    created_at: Mapped[datetime | None] = mapped_column(default=datetime.now)
