from django.urls import path

from .views import *

urlpatterns = [
    path("", ListView.as_view(), name="log_read"),
    path("delete/", delete_with_id, name='log_delete'),
    path("update/", update_with_id, name='record_update'),

    path("log_type/<int:pk>/", log_type_view, name="log_type"),
    path("create/", create, name='log_create'),
]
