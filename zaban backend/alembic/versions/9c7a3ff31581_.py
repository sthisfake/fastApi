"""empty message

Revision ID: 9c7a3ff31581
Revises: df9dca664ef3
Create Date: 2023-05-23 21:11:58.279294

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData
from db.db_setup import Base

import os 
import json

# revision identifiers, used by Alembic.
revision = '9c7a3ff31581'
down_revision = 'df9dca664ef3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    metadata = Base.metadata

    metadata.bind = op.get_bind()

    movies = Table('course', metadata)

    with open(os.path.join(os.path.dirname(__file__) , "../data/courses.json" ) , encoding='utf-8' ) as f:
        course_data = f.read()

    op.bulk_insert(movies , json.loads(course_data))    
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
