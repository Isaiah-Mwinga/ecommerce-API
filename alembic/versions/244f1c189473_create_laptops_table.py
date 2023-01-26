"""create Laptops table

Revision ID: 244f1c189473
Revises: fee13c022ffb
Create Date: 2023-01-26 21:56:06.990011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '244f1c189473'
down_revision = 'fee13c022ffb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "Laptops",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("description", sa.String(255), nullable=False),
        sa.Column("image", sa.String(255), nullable=False),
        sa.Column("category_id", sa.Integer, sa.ForeignKey("categories.id"), nullable=False),
        sa.Column("Computing_id", sa.Integer, sa.ForeignKey("Computing.id"), nullable=False),
    )


def downgrade():
    op.drop_table("Laptops")
