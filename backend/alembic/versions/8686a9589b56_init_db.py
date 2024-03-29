"""Init db

Revision ID: 8686a9589b56
Revises: 
Create Date: 2023-04-10 17:53:14.217870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8686a9589b56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_note_id'), 'note', ['id'], unique=False)
    op.create_index(op.f('ix_note_title'), 'note', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_note_title'), table_name='note')
    op.drop_index(op.f('ix_note_id'), table_name='note')
    op.drop_table('note')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
