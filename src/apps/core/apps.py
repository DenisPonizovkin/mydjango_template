from django.apps                                import AppConfig
from pathlib                                    import Path

# custom libs

from src.settings.log_settings                  import LOG_DIR

class CoreConfig(AppConfig):
    name    = 'src.apps.core'
    label   = 'core'

    def ready(self):
        Path(LOG_DIR).mkdir(parents=True, exist_ok=True)