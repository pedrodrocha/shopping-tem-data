"""create brands table

Revision ID: bedf0a3696e1
Revises: e72e9042a7ab
Create Date: 2023-07-04 19:00:15.127417

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.mysql import BIGINT

from classes.AlembicHelper import AlembicHelper

# revision identifiers, used by Alembic.
revision = "bedf0a3696e1"
down_revision = "e72e9042a7ab"
branch_labels = None
depends_on = None


def upgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists("brands")
    if table_exists is False:
        op.create_table(
            "brands",
            sa.Column(
                "id", BIGINT(unsigned=True),
                primary_key=True, autoincrement= True,
            ),
            sa.Column("name", sa.String(255), unique=True),
            sa.Column("description", sa.String(255)),
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
    table_exists = helper.table_exists("brands")
    if table_exists is True:
        op.drop_table("brands")
