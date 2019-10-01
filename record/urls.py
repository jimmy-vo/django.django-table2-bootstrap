from django.urls import include, path

from record.views import *


urlpatterns = [
    path("", FilteredPersonListView.as_view(), name="filtertableview"),
    path("country/<int:pk>/", country_detail, name="country_detail"),
    path("person/<int:pk>/", person_detail, name="person_detail"),
    path("validate_delete/", validate_delete, name='validate_delete'),
]