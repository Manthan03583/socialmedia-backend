"""add foreign-key to posts table

Revision ID: 4bc9b63b371e
Revises: 1866989d395f
Create Date: 2025-03-21 07:40:20.713497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4bc9b63b371e'
down_revision: Union[str, None] = '1866989d395f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )

    op.create_foreign_key(
        'post_users_fk',
        source_table="posts",
        referent_table="users",
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete="CASCADE"
    )

    pass


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')

    pass
