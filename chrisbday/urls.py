from django.urls import path

from . import views

app_name = "chrisbday"
urlpatterns = [
	path("", views.index, name="index")
]