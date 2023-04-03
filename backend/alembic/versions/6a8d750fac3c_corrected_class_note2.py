"""corrected class note2

Revision ID: 6a8d750fac3c
Revises: b514d3ae0c35
Create Date: 2023-04-01 09:50:32.788239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a8d750fac3c'
down_revision = 'b514d3ae0c35'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('note_role_id_fkey', 'note', type_='foreignkey')
    op.drop_column('note', 'role_id')
    op.drop_column('note', 'is_active')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('note', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('note_role_id_fkey', 'note', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###