"""empty message

Revision ID: bec88339e8ef
Revises: 38f8ca71e523
Create Date: 2016-08-28 11:13:01.645421

"""

# revision identifiers, used by Alembic.
revision = 'bec88339e8ef'
down_revision = '38f8ca71e523'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('custom_sys_role', 'title')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('custom_sys_role', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
