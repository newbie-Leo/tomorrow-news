from news_center.models import News
from rest_framework import serializers


class NewsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'url', 'site', 'ts',
                  'b_type', 'imageurls', 'n_abs', 'n_date',)
