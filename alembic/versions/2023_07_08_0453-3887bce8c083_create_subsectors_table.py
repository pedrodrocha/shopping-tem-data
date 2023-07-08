"""create subsectors table

Revision ID: 3887bce8c083
Revises: 031e3a621402
Create Date: 2023-07-08 04:53:46.499630

"""
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import BIGINT

from alembic import op
from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "3887bce8c083"
down_revision = "031e3a621402"
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("subsectors")

    if table_exists is False:
        op.create_table(
            "subsectors",
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement= True,
            ),
            sa.Column(
                "sector_id", BIGINT(unsigned=True),
                sa.ForeignKey("sectors.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column("subsector", sa.String(255), unique=True),
            sa.Column("description", sa.String(255), nullable=True),
            sa.Column(
                "updated_at", sa.TIMESTAMP,
                server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            ),
            sa.Column(
                "created_at", sa.TIMESTAMP,
                server_default=sa.text("CURRENT_TIMESTAMP"),
            ),
        )


def downgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("subsectors")

    if table_exists is True:
        op.drop_constraint(
            "fk_subsectors_sector_id_sectors",
            table_name="subsectors",
            type_="foreignkey",
        )
        op.drop_table("subsectors")
