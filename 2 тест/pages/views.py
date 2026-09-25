from django.shortcuts import render

from config.models import Service, Settings, Slide


DEFAULT_SERVICES = [
    {
        'title': 'Mercedes-Benz GLE',
        'description': '2024 · 3.0 / 367 л.с. · 4MATIC',
        'price': '$72 900',
        'image_url': 'https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&w=800&q=80',
        'category': 'suv',
    },
    {
        'title': 'BMW X6 M',
        'description': '2024 · 4.4 / 530 л.с. · xDrive',
        'price': '$98 500',
        'image_url': 'https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?auto=format&fit=crop&w=800&q=80',
        'category': 'suv',
    },
    {
        'title': 'Porsche Taycan',
        'description': '2025 · Electric / 625 л.с. · AWD',
        'price': '$115 000',
        'image_url': 'https://images.unsplash.com/photo-1617814076367-b759c7d7e738?auto=format&fit=crop&w=800&q=80',
        'category': 'electric',
    },
]

DEFAULT_SLIDES = [
    {
        'title': 'Найди свой идеальный автомобиль',
        'description': 'Более 200 проверенных автомобилей в наличии. Тест-драйв, trade-in и кредит за один визит.',
        'image_url': 'https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1600&q=80',
        'button_text': 'Смотреть каталог',
        'button_url': '/catalog/',
    },
]


def get_services():
    services = []
    for service in Service.objects.all():
        services.append({
            'title': service.title,
            'description': service.description,
            'price': service.price,
            'image_url': service.image.url if service.image else '',
            'category': 'all',
        })
    return services or DEFAULT_SERVICES


def get_slides():
    slides = []
    for slide in Slide.objects.filter(is_active=True):
        slides.append({
            'title': slide.title,
            'description': slide.description,
            'image_url': slide.image.url if slide.image else '',
            'button_text': slide.button_text,
            'button_url': slide.button_url,
        })
    return slides or DEFAULT_SLIDES


def get_site_settings():
    return Settings.objects.first()

def home(request):
    services = get_services()
    return render(request, 'pages/index.html', {
        'services': services[:3],
        'slides': get_slides(),
        'site_settings': get_site_settings(),
    })


def catalog(request):
    return render(request, 'pages/catalog.html', {
        'services': get_services(),
        'site_settings': get_site_settings(),
    })


def about(request):
    return render(request, 'pages/about.html', {'site_settings': get_site_settings()})


def services(request):
    return render(request, 'pages/catalog.html', {
        'services': get_services(),
        'site_settings': get_site_settings(),
    })


def contacts(request):
    return render(request, 'pages/contacts.html', {'site_settings': get_site_settings()})
