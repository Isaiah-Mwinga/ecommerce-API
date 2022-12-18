"""create Users table

Revision ID: 0b27a1772062
Revises: 
Create Date: 2022-12-18 09:31:27.252393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b27a1772062'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('password', sa.String),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade() -> None:
    pass
