"""merge 22ab1917044f and 87d6792f45b

Revision ID: 6deff5f9b388
Revises: 22ab1917044f, e87d6792f45b
Create Date: 2025-02-28 16:16:24.682234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6deff5f9b388'
down_revision: Union[str, None] = ('22ab1917044f', 'e87d6792f45b')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
