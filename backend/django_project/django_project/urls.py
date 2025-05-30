from django.contrib import admin
from django.urls import path
from django_app.views import hello_rest_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello_rest_api, name='hello_rest_api'),
]
