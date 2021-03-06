"""mecanicaRapida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path, path
from registro import views
from registro.views import HomeIndex

#'C:\\Users\\6005220\\source\\mecanicaRapida\\registro\\urls.py'>, 'registro', 'registro'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('registro.urls'),name="registro"),
    path('', HomeIndex.as_view()),
]
#print("(****{")
#print(include('registro.urls'))
#print(urlpatterns)
#print("(****}")
   #path(r'^',include('registro.urls')),
#    path('registro/',views.IndexView.as_view(),name="index"),
