"""create subsectors_brands table

Revision ID: bafc8af5b8ed
Revises: ada775e88053
Create Date: 2023-07-08 05:12:16.083782

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.mysql import BIGINT

from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "bafc8af5b8ed"
down_revision = "ada775e88053"
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("subsectors_brands")

    if table_exists is False:
        op.create_table(
            "subsectors_brands",
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement= True,
            ),
            sa.Column(
                "brand_id", BIGINT(unsigned=True),
                sa.ForeignKey("brands.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column(
                "subsector_id", BIGINT(unsigned=True),
                sa.ForeignKey("subsectors.id", ondelete="CASCADE"), nullable=False,
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
    table_exists = helper.table_exists("subsectors_brands")

    if table_exists is True:
        op.drop_constraint(
            "fk_subsectors_brands_brand_id_brands",
            table_name="subsectors_brands",
            type_="foreignkey",
        )
        op.drop_constraint(
            "fk_subsectors_brands_subsector_id_subsectors",
            table_name="subsectors_brands",
            type_="foreignkey",
        )
        op.drop_table("subsectors_brands")
