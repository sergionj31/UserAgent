from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexer, name='index'),
    path('info', views.infoView, name='info'),
    path('visit', views.visiter, name='visit'),
]