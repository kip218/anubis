"""initial_autogenerate

Revision ID: 71351d888a26
Revises:
Create Date: 2023-06-08 20:15:48.033756

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "71351d888a26"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "guilds",
        sa.Column("guild_id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("github_organization", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("guild_id"),
    )
    op.create_table(
        "roles_permissions",
        sa.Column("roles_permissions_id", sa.BigInteger(), nullable=False),
        sa.Column("guild_id", sa.BigInteger(), nullable=False),
        sa.Column("role_id", sa.BigInteger(), nullable=False),
        sa.Column("permission", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("roles_permissions_id"),
    )
    op.create_table(
        "users",
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("todo_list", sa.PickleType(), nullable=False),
        sa.PrimaryKeyConstraint("user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    op.drop_table("roles_permissions")
    op.drop_table("guilds")
    # ### end Alembic commands ###
