"""criando tabelas

Revision ID: 011df100f5db
Revises: 
Create Date: 2025-07-13 01:27:34.382792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '011df100f5db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('telefone', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('agendamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.Column('inicio', sa.DateTime(), nullable=False),
    sa.Column('fim', sa.DateTime(), nullable=False),
    sa.Column('finalizado_em', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agendamento')
    op.drop_table('cliente')
    # ### end Alembic commands ###
