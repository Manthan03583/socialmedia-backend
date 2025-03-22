"""add content column to post table

Revision ID: fb51d64bf7e9
Revises: d633d1debe62
Create Date: 2025-03-20 22:06:05.467451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb51d64bf7e9'
down_revision: Union[str, None] = 'd633d1debe62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )
    
    pass


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        'posts',
        'content'
    )

    pass
