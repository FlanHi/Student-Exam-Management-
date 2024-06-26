"""Relationship

Revision ID: 88e3d76e2bbb
Revises: 32c19726da6c
Create Date: 2023-11-16 14:26:42.539846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88e3d76e2bbb'
down_revision = '32c19726da6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exams', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_exams_user_id_user'), 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exams', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_exams_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
