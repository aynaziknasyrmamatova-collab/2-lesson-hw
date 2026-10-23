from django.apps import AppConfig


class RoomsConfig(AppConfig):
    name = 'rooms'
    verbose_name = "Комнаты"

    def ready(self):
        import rooms.signals
