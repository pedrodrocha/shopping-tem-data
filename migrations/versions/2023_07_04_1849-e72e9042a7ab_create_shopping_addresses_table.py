"""create shopping_addresses table

Revision ID: e72e9042a7ab
Revises: 9a8b063556cc
Create Date: 2023-07-04 18:49:58.749460

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.mysql import BIGINT, INTEGER

from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "e72e9042a7ab"
down_revision = "e661f1b28b09"
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("shopping_addresses")
    if table_exists is False:
        op.create_table(
            "shopping_addresses",
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement=True,
            ),
            sa.Column(
                "shopping_id", BIGINT(unsigned=True),
                sa.ForeignKey("shoppings.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column("address_line_1", sa.String(255)),
            sa.Column("address_line_2", sa.String(255), nullable=True),
            sa.Column(
                "state_id", BIGINT(unsigned=True),
                sa.ForeignKey("states.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column(
                "city_id", BIGINT(unsigned=True),
                sa.ForeignKey("cities.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column("postal_code", INTEGER(unsigned=True)),
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
    table_exists = helper.table_exists("shopping_addresses")
    if table_exists is True:
        op.drop_table("shopping_addresses")
