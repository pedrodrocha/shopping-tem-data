"""Create shopping_phones table

Revision ID: 2bccf1bcc1cc
Revises: a18d7122bdc2
Create Date: 2023-06-25 08:56:24.622340

"""
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import BIGINT

from alembic import op
from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "2bccf1bcc1cc"
down_revision = "a18d7122bdc2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("shopping_phones")
    if table_exists is False:
        op.create_table(
            "shopping_phones",
             sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement= True,
            ),
             sa.Column(
                "shopping_id", BIGINT(unsigned=True),
                sa.ForeignKey("shoppings.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column(
                "phone", BIGINT(unsigned=True),
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
    table_exists = helper.table_exists("shopping_phones")
    if table_exists is True:
        op.drop_constraint(
            "fk_shopping_phones_shopping_id_shoppings",
            table_name="shopping_phones",
            type_="foreignkey",
        )
        op.drop_table("shopping_phones")
