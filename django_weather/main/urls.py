from django.urls import path
from . import views
from .api import SearchHistoryListView

urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path('api/', SearchHistoryListView.as_view(), name='api')
]
