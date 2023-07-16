"""create cities table

Revision ID: e661f1b28b09
Revises: bafc8af5b8ed
Create Date: 2023-07-16 07:27:04.346934

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.mysql import BIGINT

from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "e661f1b28b09"
down_revision = "cde668d041d2"
branch_labels = None
depends_on = None

def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("cities")
    if table_exists is False:
        op.create_table(
            "cities",
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement=True,
            ),
            sa.Column(
                "state_id", BIGINT(unsigned=True),
                sa.ForeignKey("states.id", ondelete="CASCADE"), nullable=False,
            ),
            sa.Column(
                "code", BIGINT(unsigned=True), nullable=False,
            ),
            sa.Column("city", sa.String(255), nullable=False),
            sa.Column(
                "updated_at", sa.TIMESTAMP,
                server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            ),
            sa.Column(
                "created_at", sa.TIMESTAMP,
                server_default=sa.text("CURRENT_TIMESTAMP"),
            ),
        )

        op.create_unique_constraint(
            "uq_cities_state_id_city",
            table_name="cities", columns=["state_id", "city"],
        )


def downgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("cities")
    if table_exists is True:
        op.drop_table("cities")
