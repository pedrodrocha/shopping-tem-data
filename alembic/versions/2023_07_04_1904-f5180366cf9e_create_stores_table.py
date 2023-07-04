"""create stores table

Revision ID: f5180366cf9e
Revises: bedf0a3696e1
Create Date: 2023-07-04 19:04:13.368723

"""
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import BIGINT

from alembic import op
from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "f5180366cf9e"
down_revision = "bedf0a3696e1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("stores")

    if table_exists is False:
        op.create_table(
            "stores",
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement= True,
            ),
            sa.Column(
                "shopping_id", BIGINT(unsigned=True),
                sa.ForeignKey("shoppings.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column(
                "brand_id", BIGINT(unsigned=True),
                sa.ForeignKey("brands.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column("location", sa.String(255), nullable=True),
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
    table_exists = helper.table_exists("stores")

    if table_exists is True:
        op.drop_constraint(
            "fk_stores_shopping_id_shoppings",
            table_name="stores",
            type_="foreignkey",
        )
        op.drop_constraint(
            "fk_stores_brand_id_brands",
            table_name="stores",
            type_="foreignkey",
        )
        op.drop_table("stores")
