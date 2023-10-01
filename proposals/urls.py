from django.urls import path

from proposals import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
]