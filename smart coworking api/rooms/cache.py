from hashlib import sha256
from uuid import uuid4

from django.core.cache import cache


ROOM_LIST_CACHE_VERSION_KEY = "rooms:list:cache-version"
ROOM_LIST_CACHE_TIMEOUT = 60


def invalidate_room_list_cache():
    cache.set(ROOM_LIST_CACHE_VERSION_KEY, uuid4().hex, timeout=None)


def get_room_list_cache_key(request):
    version = cache.get(ROOM_LIST_CACHE_VERSION_KEY, "initial")
    visibility = "staff" if request.user.is_staff else "public"
    value = f"{version}:{visibility}:{request.get_full_path()}"
    digest = sha256(value.encode("utf-8")).hexdigest()
    return f"rooms:list:{digest}"
