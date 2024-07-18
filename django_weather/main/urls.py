from django.urls import path
from . import views
from .api import SearchHistoryListView

urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path('about-api', views.about_api, name='about-api'),
    path('about-site', views.about_site, name='about-site'),
    path('api/', SearchHistoryListView.as_view(), name='api'),
]
