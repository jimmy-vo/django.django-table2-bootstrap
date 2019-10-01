from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export import ExportMixin
from .models import *
from .table import *
from .filters import *


class FilteredPersonListView(ExportMixin, SingleTableMixin, FilterView):
    template_name = "bootstrap_template.html"
    table_class = PersonTable
    model = Person
    filterset_class = PersonFilter
    export_formats = ("csv", "xls")

    def get_queryset(self):
        return super().get_queryset().select_related("country")

    def get_table_kwargs(self):
        return {"template_name": "django_tables2/bootstrap.html"}


def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    table = PersonTable(country.person_set.all(), extra_columns=(("country", None),))
    return render(request, "country_detail.html", {"country": country, "table": table})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)

    return render(request, "person_detail.html", {"person": person})


def validate_delete(request):
    id = request.GET.get('id', None)
    # if Person.objects.filter(id__iexact=id).exists():
    data = {
        'result': Person.objects.filter(id__iexact=id).exists()
    }
    return JsonResponse(data)

