"""Create shoppings table

Revision ID: a18d7122bdc2
Revises: 
Create Date: 2023-06-24 14:43:40.680666

"""
from classes.AlembicHelper import AlembicHelper
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a18d7122bdc2'
down_revision = None
branch_labels = None
depends_on = None



def upgrade() -> None:    
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists('shoppings')

    if table_exists is False:
        op.create_table(
            'shoppings',
             sa.Column('id', sa.Integer, primary_key=True),
        )



def downgrade() -> None:
    helper = AlembicHelper(conn=op.get_bind())
    table_exists = helper.table_exists('shoppings')

    if table_exists is True:
        op.drop_table('shoppings')

