import logging
from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults

log = logging.getLogger(__name__)


class HelloWorldOperator(BaseOperator):

    @apply_defaults
    def __init__(self, my_params, *args, **kwargs):
        self.my_params = my_params
        super(HelloWorldOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('Hello World!')
        log.info('My params: {}'.format(self.my_params))


class HelloWorldPlugin(AirflowPlugin):
    name = 'hello_world_plugin'
    operators = [HelloWorldOperator]