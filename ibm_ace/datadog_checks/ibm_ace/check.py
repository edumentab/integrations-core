# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pymqi

from datadog_checks.base import AgentCheck

from .config_models import ConfigMixin
from .subscription import FlowMonitoringSubscription, ResourceStatisticsSubscription


class IbmAceCheck(AgentCheck, ConfigMixin):
    __NAMESPACE__ = 'ibm_ace'

    def __init__(self, name, init_config, instances):
        super(IbmAceCheck, self).__init__(name, init_config, instances)

        self._tags = None
        self._connection_options = None
        self._queue_manager = None
        self._subscriptions = None

        self.check_initializations.append(self.initialize_config)
        self.check_initializations.append(self.set_up_subscriptions)

    def check(self, _):
        try:
            for subscription in self._subscriptions:
                subscription.collect()
        finally:
            if not self.config.persist_connections:
                self.disconnect()

    def initialize_config(self):
        tags = [f'mq_server:{self.config.mq_server}', f'mq_port:{self.config.mq_port}', *self.config.tags]
        self._tags = tuple(tags)

        channel_definition = pymqi.CD()
        channel_definition.ChannelName = self.config.channel.encode('utf-8')
        channel_definition.ConnectionName = f'{self.config.mq_server}({self.config.mq_port})'.encode('utf-8')
        channel_definition.ChannelType = pymqi.CMQC.MQCHT_CLNTCONN
        channel_definition.TransportType = pymqi.CMQC.MQXPT_TCP
        channel_definition.Version = getattr(pymqi.CMQC, f'MQCD_VERSION_{self.config.mqcd_version}')
        self._connection_options = {
            'cd': channel_definition,
            'user': self.config.mq_user,
            'password': self.config.mq_password,
        }

    def set_up_subscriptions(self):
        subscriptions = []

        if self.config.resource_statistics:
            subscriptions.append(ResourceStatisticsSubscription(self, self._tags))

        if self.config.message_flows:
            subscriptions.append(FlowMonitoringSubscription(self, self._tags))

        self._subscriptions = subscriptions

    @property
    def queue_manager(self):
        if self._queue_manager is None:
            queue_manager = pymqi.QueueManager(None)
            cd = self._connection_options['cd']
            self.log.info(
                'Connecting to MQ: connection=%s | queue manager=%s | channel=%s | user=%s',
                cd.ConnectionName.decode('utf-8'),
                self.config.queue_manager,
                self.config.channel,
                self.config.mq_user,
            )
            queue_manager.connect_with_options(self.config.queue_manager, **self._connection_options)
            self._queue_manager = queue_manager

        return self._queue_manager

    def disconnect(self):
        for subscription in self._subscriptions:
            subscription.disconnect()

        if self._queue_manager is not None:
            self._queue_manager.disconnect()
            self._queue_manager = None

    def cancel(self):
        self.disconnect()
