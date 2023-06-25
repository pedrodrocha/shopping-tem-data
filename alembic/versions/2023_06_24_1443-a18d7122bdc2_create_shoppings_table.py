"""Create shoppings table.

Revision ID: a18d7122bdc2
Revises:
Create Date: 2023-06-24 14:43:40.680666

"""
import sqlalchemy as sa

from alembic import op
from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "a18d7122bdc2"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None: #noqa: D203
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("shoppings")

    if table_exists is False:
        op.create_table(
            "shoppings",
             sa.Column(
                "id", sa.Integer,
                primary_key=True, autoincrement= True,
            ),
             sa.Column("name", sa.String(255)),
             sa.Column("site_url", sa.String(255)),
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
    table_exists = helper.table_exists("shoppings")

    if table_exists is True:
        op.drop_table("shoppings")
