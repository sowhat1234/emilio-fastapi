"""add content column to posts table

Revision ID: bd920108494d
Revises: be58bd396704
Create Date: 2021-12-14 17:40:07.287642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd920108494d'
down_revision = 'be58bd396704'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
