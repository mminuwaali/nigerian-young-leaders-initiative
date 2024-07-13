from . import views
from django.urls import path

app_name, urlpatterns = "landing", [
    path("", views.index_view, name="index-view"),
    path("team/", views.team_view, name="team-view"),
    path("apply/", views.apply_view, name="apply-view"),
    path("about-us/", views.about_view, name="about-view"),
    path("donate/", views.donate_view, name="donate-view"),
    path("student/", views.student_view, name="student-view"),
    path("contact-us/", views.contact_view, name="contact-view"),
    path("team/<id>/", views.team_detail_view, name="team-detail-view"),
]
