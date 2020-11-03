"""empty message

Revision ID: 0f053e41a8d9
Revises: 581eacfd7ff0
Create Date: 2020-11-02 23:05:20.832134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f053e41a8d9'
down_revision = '581eacfd7ff0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('photo', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'photo')
    # ### end Alembic commands ###
