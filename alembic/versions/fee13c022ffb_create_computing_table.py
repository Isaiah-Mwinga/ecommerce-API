"""create Computing table

Revision ID: fee13c022ffb
Revises: 415fa9968816
Create Date: 2023-01-20 22:19:30.057998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fee13c022ffb'
down_revision = '415fa9968816'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "computing",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String, unique=True, index=True),
        sa.Column("category_id", sa.Integer, sa.ForeignKey("categories.id")),
    )


def downgrade() -> None:
    op.drop_table("computing")
