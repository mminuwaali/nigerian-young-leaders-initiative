from . import views
from django.urls import path

app_name, urlpatterns = "program", [
    path("", views.index_view, name="index-view"),
    path("<id>/", views.detail_view, name="detail-view"),
]
