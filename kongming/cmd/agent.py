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

"""The KongMing agent Service."""

import sys

from oslo_config import cfg
from oslo_service import service

from kongming.common import constants
from kongming.common import service as kongming_service


CONF = cfg.CONF


def main():
    # Parse config file and command line options, then start logging
    kongming_service.prepare_service(sys.argv)

    mgr = kongming_service.RPCService('kongming.agent.manager',
                                      'AgentManager',
                                      constants.AGENT_TOPIC,
                                      init_notification_listener=True)

    launcher = service.launch(CONF, mgr)
    launcher.wait()
