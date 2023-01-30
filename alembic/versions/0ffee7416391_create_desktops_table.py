"""create Desktops table

Revision ID: 0ffee7416391
Revises: 244f1c189473
Create Date: 2023-01-30 21:43:35.223950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ffee7416391'
down_revision = '244f1c189473'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Desktops',
       sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("description", sa.String(255), nullable=False),
        sa.Column("image", sa.String(255), nullable=False),
        sa.Column("category_id", sa.Integer, sa.ForeignKey("categories.id"), nullable=False),
        sa.Column("Computing_id", sa.Integer, sa.ForeignKey("Computing.id"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('Desktops')
