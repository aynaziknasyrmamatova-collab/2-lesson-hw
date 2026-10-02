from django.urls import path
from .views import Hell, hello_api, People
urlpatterns=[
    path("hello/", Hell.as_view(), name="hello-message"),
    path ('func/',hello_api,name="hello-func"),
    path ('people/', People.as_view(),name="people-message"),
]