
from django.apps import AppConfig

from .widget.countdown.models import CountdownWidget
from .widget.counter.models import CounterWidget

default_app_config = 'leonardo_counters.Config'


LEONARDO_APPS = ['leonardo_counters']

LEONARDO_WIDGETS = [CounterWidget, CountdownWidget]

LEONARDO_JS_FILES = [
    'js/lib/jquery.counter.js',
    'js/lib/jquery.appear.js',
]
LEONARDO_OPTGROUP = "Counters"


class Config(AppConfig):
    name = 'leonardo_counters'
    verbose_name = "Leonardo Counters"
