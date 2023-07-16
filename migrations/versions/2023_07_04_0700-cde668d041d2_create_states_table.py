"""create states table

Revision ID: cde668d041d2
Revises: bafc8af5b8ed
Create Date: 2023-07-16 07:25:14.141266

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.mysql import BIGINT

from classes.AlembicHelper import AlembicHelper


# revision identifiers, used by Alembic.
revision = 'cde668d041d2'
down_revision = '9a8b063556cc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("states")
    if table_exists is False:
        op.create_table(
            'states',
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement=True,
            ),
            sa.Column("abbr", sa.String(255)),
            sa.Column("state", sa.String(255), nullable=True),
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
            "uq_states_abbr_state",
            table_name="states", columns=["abbr", "state"],
        )


def downgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("states")
    if table_exists is True:
        op.drop_table("states")

