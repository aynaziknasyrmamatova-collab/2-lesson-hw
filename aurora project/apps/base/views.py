from django.shortcuts import render

from apps.base.models import Settings
# Create your views here.

def index(request):
    settings = Settings.objects.first()
    return render(request, "index.html", locals())
def rooms(request):
    settings = Settings.objects.first()
    return render(request, "rooms.html", locals())


def contact(request):
    settings = Settings.objects.first()
    return render(request, "contact.html", locals())