from django_filters import FilterSet

from .models import Log


class Filter(FilterSet):
    class Meta:
        model = Log
        fields = {"time": ["contains"], "log_type": ["exact"], "info": ["contains"]}
