from news_center.models import News
from rest_framework import viewsets
from restapi.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
