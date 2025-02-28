"""merge 18248d276e64 and 7db7efdce183

Revision ID: 99ce0f4ca2c7
Revises: 18248d276e64, 7db7efdce183
Create Date: 2025-02-28 06:23:53.769099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99ce0f4ca2c7'
down_revision: Union[str, None] = ('18248d276e64', '7db7efdce183')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
