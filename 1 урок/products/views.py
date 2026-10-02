from rest_framework.generics import ListCreateAPIView

from .models import Product
from .serializers import ProductsSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer