
from django.apps import AppConfig

try:
    from local_settings import APPS
except ImportError:
    pass

default_app_config = 'leonardo_counters.Config'

if 'leonardo_counters' in APPS:
    LEONARDO_APPS = ['leonardo_counters']

    LEONARDO_WIDGETS = ['leonardo_counters.models.CounterWidget',
                        'leonardo_counters.models.CountdownWidget']

    LEONARDO_JS_FILES = [
        'js/lib/jquery.counter.js',
        'js/lib/jquery.appear.js',
    ]
    LEONARDO_OPTGROUP = "Counters"


class Config(AppConfig):
    name = 'leonardo_counters'
    verbose_name = "Leonardo Counters"
