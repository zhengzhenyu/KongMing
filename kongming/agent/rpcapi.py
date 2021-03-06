# Copyright 2016 Huawei Technologies Co.,LTD.
# All Rights Reserved.
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
"""
Client side of the agent RPC API.
"""
from oslo_config import cfg
import oslo_messaging as messaging

from kongming.common import constants
from kongming.common import rpc
from kongming.objects import base as objects_base

CONF = cfg.CONF


class EngineAPI(object):
    """Client side of the engine RPC API.

    API version history:

    |    1.0 - Initial version.

    """

    RPC_API_VERSION = '1.0'

    def __init__(self, topic=None):
        super(EngineAPI, self).__init__()
        self.topic = topic
        if self.topic is None:
            self.topic = constants.AGENT_TOPIC

        target = messaging.Target(topic=self.topic,
                                  version='1.0')
        serializer = objects_base.KongmingObjectSerializer()
        self.client = rpc.get_client(target,
                                     version_cap=self.RPC_API_VERSION,
                                     serializer=serializer)

    def update_instance_cpu_mapping(self, context, mapping):
        cctxt = self.client.prepare(server=mapping.host,
                                    version=self.RPC_API_VERSION)
        return cctxt.call(context, 'adjust_instance_cpu_mapping',
                          mapping=mapping)
