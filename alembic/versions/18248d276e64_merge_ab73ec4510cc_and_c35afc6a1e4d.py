"""merge ab73ec4510cc and c35afc6a1e4d

Revision ID: 18248d276e64
Revises: ab73ec4510cc, c35afc6a1e4d
Create Date: 2025-02-28 06:16:20.254881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18248d276e64'
down_revision: Union[str, None] = ('ab73ec4510cc', 'c35afc6a1e4d')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
