#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""initial migration.

Revision ID: f50980397351
Revises: None
Create Date: 2018-05-26 08:44:36.010417

"""


from alembic import op
import sqlalchemy as sa
from sqlalchemy import Text


# revision identifiers, used by Alembic.
revision = 'f50980397351'
down_revision = None


def upgrade():
    op.create_table(
        'instance_cpu_mappings',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('instance_uuid', sa.String(length=36), nullable=False),
        sa.Column('project_id', sa.String(length=36), nullable=False),
        sa.Column('user_id', sa.String(length=36), nullable=False),
        sa.Column('host', sa.String(length=255), nullable=True),
        sa.Column('status', sa.String(length=255), nullable=True),
        sa.Column('cpu_mappings', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('instance_uuid',
                            name='uniq_mappings0instance_uuid'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_table(
        'hosts',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('host_name', sa.String(length=255), nullable=True),
        sa.Column('cpu_topology', Text, nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('host_name',
                            name='uniq_hosts0host_name'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_table(
        'instances',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('uuid', sa.String(length=36), nullable=False),
        sa.Column('host', sa.String(length=255), nullable=True),
        sa.Column('status', sa.String(length=255), nullable=True),
        sa.Column('cpu_mappings', Text, nullable=True),
        sa.ForeignKeyConstraint(['host'], ['hosts.host_name']),
        sa.PrimaryKeyConstraint('uuid'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
