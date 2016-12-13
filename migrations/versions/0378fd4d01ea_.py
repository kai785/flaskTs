"""empty message

Revision ID: 0378fd4d01ea
Revises: None
Create Date: 2016-12-13 23:22:47.162920

"""

# revision identifiers, used by Alembic.
revision = '0378fd4d01ea'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'age')
    ### end Alembic commands ###
