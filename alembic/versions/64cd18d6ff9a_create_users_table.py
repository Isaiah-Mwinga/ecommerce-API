"""create users table

Revision ID: 64cd18d6ff9a
Revises: 
Create Date: 2023-01-12 11:34:55.315836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64cd18d6ff9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('password', sa.String),
        sa.Column('email', sa.String, unique=True),
    )


def downgrade():
    op.drop_table('users')
