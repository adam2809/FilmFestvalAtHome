from django.apps import AppConfig
from datadog import initialize, statsd


class FFHomeConfig(AppConfig):
    name = 'ffhome'
    def ready(self):
        initialize()
