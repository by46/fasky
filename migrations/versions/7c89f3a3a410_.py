"""empty message

Revision ID: 7c89f3a3a410
Revises: 229f1ddaed4d
Create Date: 2016-08-29 18:11:30.858000

"""

# revision identifiers, used by Alembic.
revision = '7c89f3a3a410'
down_revision = '229f1ddaed4d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
