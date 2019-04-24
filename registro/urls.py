from django.urls import path, re_path
from . import views

app_name = "registro"

urlpatterns = [
    path("registro/",views.IndexView.as_view(),name="registro")
]