from django.urls import path
from . import views

urlpatterns = [
    path('', views.empty_api, name='empty_api'),
]
