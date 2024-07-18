from rest_framework import generics
from .models import SearchHistory
from .serializers import SearchHistorySerializer


class SearchHistoryListView(generics.ListCreateAPIView):
    serializer_class = SearchHistorySerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = SearchHistory.objects.all()
        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city=city)
        return queryset
