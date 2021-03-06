"""empty message

Revision ID: 6b1af86c59b8
Revises: 6a07c4341f97
Create Date: 2021-04-21 17:12:51.164733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b1af86c59b8'
down_revision = '6a07c4341f97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts_tags',
    sa.Column('posts_id', sa.Integer(), nullable=True),
    sa.Column('tags_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['posts_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tags_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts_tags')
    # ### end Alembic commands ###
