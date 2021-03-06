"""empty message

Revision ID: 3ab3f07228f5
Revises: a2a0259d29f4
Create Date: 2021-10-08 21:43:30.739154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ab3f07228f5'
down_revision = 'a2a0259d29f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('Artist', 'seeking_venues')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venues', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
