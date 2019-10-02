from django.urls import include, path

from record.views import *


urlpatterns = [
    path("", FilteredPersonListView.as_view(), name="filtertableview"),
    path("country/<int:pk>/", country_detail, name="country_detail"),
    path("person/<int:pk>/", person_detail, name="person_detail"),
    path("ajax_delete/", ajax_delete, name='ajax_delete'),
    path("ajax_update/", ajax_update, name='ajax_update'),
]

