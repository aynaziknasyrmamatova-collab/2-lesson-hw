from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

def product_list_view(request):
    
    page_number = int(request.GET.get('page', 1))
    per_page = 500  
    start = (page_number - 1) * per_page
    end = start + per_page
    
    queryset = Product.objects.all().order_by('id')
    paginator = Paginator(queryset, per_page=per_page)
    page_obj = paginator.get_page(page_number)
    
    current_page_queryset = Product.objects.all().order_by('id')[start:end].iterator(chunk_size=500)
    
    products_list = [
        {"id": p.id, "title": p.title, "description": p.description} 
        for p in current_page_queryset
    ]
    
    return render(request, 'products.html', {
        'page_obj': page_obj,
        'products_list': products_list
    })
