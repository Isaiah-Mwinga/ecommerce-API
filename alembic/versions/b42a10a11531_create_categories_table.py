"""create categories table

Revision ID: b42a10a11531
Revises: 8c01559585bd
Create Date: 2023-01-09 11:46:43.452413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b42a10a11531'
down_revision = '8c01559585bd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column("description", sa.String, unique=True, index=True, nullable=False),
    )
    pass


def downgrade():
    op.drop_tabl('categories')
