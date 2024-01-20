import os

IS_PRODUCTION = bool(os.environ.get('IS_PRODUCTION', 0))

if IS_PRODUCTION:
    from .settings_production import *
else:
    from .settings_development import *
