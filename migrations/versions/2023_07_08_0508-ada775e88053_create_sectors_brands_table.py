"""create sectors_brands table

Revision ID: ada775e88053
Revises: 3887bce8c083
Create Date: 2023-07-08 05:08:34.425657

"""
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import BIGINT

from alembic import op
from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "ada775e88053"
down_revision = "3887bce8c083"
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("sectors_brands")

    if table_exists is False:
        op.create_table(
            "sectors_brands",
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement= True,
            ),
            sa.Column(
                "brand_id", BIGINT(unsigned=True),
                sa.ForeignKey("brands.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column(
                "sector_id", BIGINT(unsigned=True),
                sa.ForeignKey("sectors.id", ondelete="CASCADE"), nullable=False,
            ),
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
    table_exists = helper.table_exists("sectors_brands")

    if table_exists is True:
        op.drop_constraint(
            "fk_sectors_brands_brand_id_brands",
            table_name="sectors_brands",
            type_="foreignkey",
        )
        op.drop_constraint(
            "fk_sectors_brands_sector_id_sectors",
            table_name="sectors_brands",
            type_="foreignkey",
        )
        op.drop_table("sectors_brands")
