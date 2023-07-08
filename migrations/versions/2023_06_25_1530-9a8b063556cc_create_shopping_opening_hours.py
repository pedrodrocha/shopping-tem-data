"""Create shopping_opening_hours table

Revision ID: 9a8b063556cc
Revises: 2bccf1bcc1cc
Create Date: 2023-06-25 15:30:30.466666

"""
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import BIGINT, ENUM, TIME

from alembic import op
from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "9a8b063556cc"
down_revision = "2bccf1bcc1cc"
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("shopping_opening_hours")
    if table_exists is False:
        op.create_table(
            "shopping_opening_hours",
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement= True,
            ),
            sa.Column(
                "shopping_id", BIGINT(unsigned=True),
                sa.ForeignKey("shoppings.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column(
                "week_day",
                ENUM(
                    "sunday","monday",
                    "tuesday","wednesday",
                    "thursday","friday", "saturday",
                ),
            ),
            sa.Column("opening_hour", TIME),
            sa.Column("closing_hour", TIME),
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
    table_exists = helper.table_exists("shopping_opening_hours")
    if table_exists is True:
        op.drop_constraint(
            "fk_shopping_opening_hours_shopping_id_shoppings",
            table_name="shopping_opening_hours",
            type_="foreignkey",
        )
        op.drop_table("shopping_opening_hours")
