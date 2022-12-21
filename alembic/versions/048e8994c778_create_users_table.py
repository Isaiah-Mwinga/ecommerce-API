"""create users table

Revision ID: 048e8994c778
Revises: 
Create Date: 2022-12-21 08:46:38.475783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '048e8994c778'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True, nullable=False),
        sa.Column("email", sa.String, unique=True, index=True, nullable=False),
        sa.Column("password", sa.String, index=True, unique=True, nullable=False),
        sa.Column("is_active", sa.Boolean, default=True, nullable=False),
    )



def downgrade() -> None:
    op.drop_table("users")
