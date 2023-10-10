
from django.urls import path
from . import views

urlpatterns = [
   path('', views.tts,name='tts')
]
