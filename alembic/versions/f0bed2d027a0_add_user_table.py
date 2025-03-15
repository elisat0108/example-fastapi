"""add user table

Revision ID: f0bed2d027a0
Revises: e6f16599b5c0
Create Date: 2025-03-14 16:47:01.963364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0bed2d027a0'
down_revision: Union[str, None] = 'e6f16599b5c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users', 
        sa.Column('id', sa.Integer(), nullable=False), 
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False), 
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                  server_default=sa.text('now()'), nullable=False),  # Fixed placement
        sa.PrimaryKeyConstraint('id')
    )

    pass

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
