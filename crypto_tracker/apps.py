from django.apps import AppConfig


class CryptoTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crypto_tracker'

    def ready(self):
        import crypto_tracker.signals