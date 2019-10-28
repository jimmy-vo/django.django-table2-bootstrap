from django.shortcuts import get_object_or_404, render
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export import ExportMixin

from . import controller
from .filters import Filter
from .models import Log, LogType
from .table import LogTable, LogTypeTable


class ListView(ExportMixin, SingleTableMixin, FilterView):
    template_name = "log.html"
    table_class = LogTable
    model = Log
    filterset_class = Filter
    export_formats = ("csv", "xls")

    def get_table_kwargs(self):
        return {"template_name": "django_tables2/bootstrap.html"}


def log_type_view(request, pk):
    company = get_object_or_404(LogType, pk=pk)
    table = LogTypeTable(company.price_set.all())
    return render(request, "log_type.html", {"log_type": log_type_view, "table": table})


def update_with_id(request):
    try:
        id, info, log_type_id = controller.validate_all(request)
        target = controller.update_with_id(id, log_type_id=log_type_id, info=info)
        return controller.get_json_ok(target)
    except Exception as e:
        return controller.get_json_error(e)


def delete_with_id(request):
    try:
        pk = controller.validate_id_exists(request)
        controller.delete_with_id(pk)
        return controller.controller.json_get_ok({'id': pk})
    except Exception as e:
        return controller.get_json_error(e)


def create(request):
    try:
        info = controller.validate_info_not_empty(request)
        target = controller.create(info)
        return controller.get_json_ok(target)
    except Exception as e:
        return controller.get_json_error(e)
