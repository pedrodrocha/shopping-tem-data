"""create store_phones table

Revision ID: ef1a369e3371
Revises: f5180366cf9e
Create Date: 2023-07-08 04:37:41.226782

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.mysql import BIGINT

from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "ef1a369e3371"
down_revision = "f5180366cf9e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("store_phones")

    if table_exists is False:
        op.create_table(
            "store_phones",
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement= True,
            ),
            sa.Column(
                "store_id", BIGINT(unsigned=True),
                sa.ForeignKey("stores.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column("phone", BIGINT(unsigned=True)),
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
    table_exists = helper.table_exists("store_phones")

    if table_exists is True:
        op.drop_constraint(
            "fk_store_phones_store_id_stores",
            table_name="store_phones",
            type_="foreignkey",
        )

        op.drop_table("store_phones")
