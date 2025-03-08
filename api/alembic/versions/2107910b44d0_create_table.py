"""create table

Revision ID: 2107910b44d0
Revises: 
Create Date: 2025-03-07 18:43:01.712466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2107910b44d0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
            "notes",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("text", sa.String),
            sa.Column("completed", sa.Boolean)
        )


def downgrade() -> None:
    op.drop_table("notes")
