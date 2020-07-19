"""update classes

Revision ID: a4f757a5aa3d
Revises: fcffb8736140
Create Date: 2020-07-17 13:49:31.930483

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a4f757a5aa3d'
down_revision = 'fcffb8736140'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('date', sa.DateTime(), nullable=False))
    op.drop_column('pitches', 'data')
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('pitches', sa.Column('data', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('pitches', 'date')
    # ### end Alembic commands ###
