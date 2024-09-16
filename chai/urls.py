from django.urls import path
from . import views

urlpatterns = [
    path('', views.chaiPage, name='chaiPage'),
]