"""add user table

Revision ID: 13f2b388cc49
Revises: bd920108494d
Create Date: 2021-12-14 17:45:15.743935

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import PrimaryKeyConstraint, UniqueConstraint


# revision identifiers, used by Alembic.
revision = '13f2b388cc49'
down_revision = 'bd920108494d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                    server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
