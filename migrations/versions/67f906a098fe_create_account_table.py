"""create account table

Revision ID: 67f906a098fe
Revises: 
Create Date: 2020-02-09 18:18:11.206123

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '67f906a098fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50)),
        sa.Column('first_name', sa.String(50), nullable=True),
        sa.Column('last_name', sa.String(50), nullable=True),
        sa.Column('password', sa.String(250)),
        sa.Column('is_active', sa.Boolean(), default=True),
        sa.Column('is_superuser', sa.Boolean(), default=False)
    )


def downgrade():
    pass
