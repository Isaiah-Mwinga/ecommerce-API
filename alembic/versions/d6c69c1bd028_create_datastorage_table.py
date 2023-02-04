"""create Datastorage  table

Revision ID: d6c69c1bd028
Revises: 0ffee7416391
Create Date: 2023-02-04 22:11:46.627073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6c69c1bd028'
down_revision = '0ffee7416391'
branch_labels = None
depends_on = None


def upgrade() :
    op.create_table(
        'Datastorage',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('description', sa.String(100), nullable=False),
        sa.Column('image', sa.String(100), nullable=False),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id'), nullable=False),
        sa.column('computing_id', sa.Integer, sa.ForeignKey('Computing.id'), nullable=False),
    )


def downgrade():
    op.drop_table('Datastorage')
