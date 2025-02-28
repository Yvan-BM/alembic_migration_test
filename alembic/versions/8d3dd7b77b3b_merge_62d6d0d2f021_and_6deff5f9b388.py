"""merge 62d6d0d2f021 and 6deff5f9b388

Revision ID: 8d3dd7b77b3b
Revises: 62d6d0d2f021, 6deff5f9b388
Create Date: 2025-02-28 16:20:49.132113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d3dd7b77b3b'
down_revision: Union[str, None] = ('62d6d0d2f021', '6deff5f9b388')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
