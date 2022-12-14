"""first alembic

Revision ID: 9a5f1aa95dde
Revises: e27e81ef2cdd
Create Date: 2022-09-08 14:48:05.674571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a5f1aa95dde'
down_revision = 'e27e81ef2cdd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('mercy', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('mercy', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
