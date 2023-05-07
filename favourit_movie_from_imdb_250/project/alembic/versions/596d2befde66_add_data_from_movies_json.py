"""Add data from movies.json

Revision ID: 596d2befde66
Revises: f2d86a63557d
Create Date: 2023-05-06 11:57:04.738051

"""
from alembic import op
import os , json
from sqlalchemy import Table, MetaData
from db.db_setup import Base


# revision identifiers, used by Alembic.
revision = '596d2befde66'
down_revision = 'f2d86a63557d'
branch_labels = None
depends_on = None


def upgrade() -> None:

    metadata = Base.metadata

    metadata.bind = op.get_bind()

    movies = Table('movie', metadata)

    with open(os.path.join(os.path.dirname(__file__) , "../data/movies.json")) as f:
        movies_data = f.read()

    op.bulk_insert(movies , json.loads(movies_data))    
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###