"""create categories table

Revision ID: 415fa9968816
Revises: 64cd18d6ff9a
Create Date: 2023-01-16 23:00:55.069860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '415fa9968816'
down_revision = '64cd18d6ff9a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        )
        


def downgrade():
    op.drop_table("categories")
