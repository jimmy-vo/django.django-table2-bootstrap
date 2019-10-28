import django_tables2 as tables

from _setting_.table import CrudTable
from .models import Log


class LogTable(CrudTable):
    id = tables.Column()
    time = tables.DateTimeColumn(short=True)
    log_type = tables.Column(linkify=True)
    info = tables.Column()

    class Meta:
        model = Log
        template_name = "django_tables2/bootstrap.html"
        sequence = ['id', 'log_type', 'time', 'info']


class LogTypeTable(LogTable):
    log_type = None
    close = tables.Column(verbose_name='Price')

    class Meta:
        model = Log
        template_name = "django_tables2/bootstrap.html"
        sequence = ['id', 'time', 'info']
