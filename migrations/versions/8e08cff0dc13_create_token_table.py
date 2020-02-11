"""create token table

Revision ID: 8e08cff0dc13
Revises: 67f906a098fe
Create Date: 2020-02-10 18:11:17.524089

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8e08cff0dc13'
down_revision = '67f906a098fe'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'token',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('token', sa.String)
    )


def downgrade():
    pass
