from django.urls import path
from .views import CategoryListCreateView,CategoryDetailView

urlpatterns = [
    path('category/', CategoryListCreateView.as_view(),name='category'),
    path('category/<int:pk>',CategoryListCreateView.as_view(),name="category")
]