from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .cache import invalidate_room_list_cache
from .models import Room


@receiver((post_save, post_delete), sender=Room)
def invalidate_room_cache_on_change(sender, **kwargs):
    invalidate_room_list_cache()
