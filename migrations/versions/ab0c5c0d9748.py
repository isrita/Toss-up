"""empty message

Revision ID: ab0c5c0d9748
Revises: 1b9d0ea15b07
Create Date: 2023-05-20 10:27:09.844610

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ab0c5c0d9748'
down_revision = '1b9d0ea15b07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('difficulty',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('instructions',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
        batch_op.drop_index('instructions')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.create_index('instructions', ['instructions'], unique=False)
        batch_op.alter_column('instructions',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('difficulty',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###