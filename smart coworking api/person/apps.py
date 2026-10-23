from django.apps import AppConfig


class PersonConfig(AppConfig):
    name = 'person'
    verbose_name = "Пользователи"

    def ready(self):
        import person.signals
