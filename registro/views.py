from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import RegisterService

 #Create your views here.
class IndexView(TemplateView):
    template_name = "registro/index.html"


class HomeIndex(ListView):
    template_name = "registro/register_service.html"
    model = RegisterService
