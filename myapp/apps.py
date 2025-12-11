from django.apps import AppConfig


class MyappConfig(AppConfig):
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    name = 'myapp'
