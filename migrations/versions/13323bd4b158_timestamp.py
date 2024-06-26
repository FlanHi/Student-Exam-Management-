"""Timestamp

Revision ID: 13323bd4b158
Revises: 88e3d76e2bbb
Create Date: 2023-11-16 14:49:01.569945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13323bd4b158'
down_revision = '88e3d76e2bbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exams', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_exams_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exams', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_exams_timestamp'))
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###
