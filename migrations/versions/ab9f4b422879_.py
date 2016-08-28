"""empty message

Revision ID: ab9f4b422879
Revises: 8df56cccad22
Create Date: 2016-08-29 02:37:53.233000

"""

# revision identifiers, used by Alembic.
revision = 'ab9f4b422879'
down_revision = '8df56cccad22'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###
