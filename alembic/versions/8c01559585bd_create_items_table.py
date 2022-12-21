"""create items table

Revision ID: 8c01559585bd
Revises: 048e8994c778
Create Date: 2022-12-21 10:12:34.061081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c01559585bd'
down_revision = '048e8994c778'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "items",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String, unique=True, index=True, nullable=False),
        sa.Column("description", sa.String, unique=True, index=True, nullable=False),
        sa.Column("price", sa.Float, index=True, unique=True, nullable=False),
        sa.Column("tax", sa.Float, index=True, unique=True, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("items")
