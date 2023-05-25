"""empty message

Revision ID: 01c9f30bcdd8
Revises: 65223f667816
Create Date: 2023-05-24 20:38:17.143090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01c9f30bcdd8'
down_revision = '65223f667816'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_course', sa.Column('phone_number_related', sa.String(length=45), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_course', 'phone_number_related')
    # ### end Alembic commands ###