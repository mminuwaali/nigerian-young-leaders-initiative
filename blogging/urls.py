from . import views
from django.urls import path

app_name, urlpatterns = "blogging", [
    path("", views.index_view, name="index-view"),
    path("<id>/", views.detail_view, name="detail-view"),
    path("category/<id>/", views.category_detail_view, name="category-detail-view"),
]
