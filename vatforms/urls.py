from django.urls import path
from . import views

urlpatterns = [
    path('create-invoice', views.createinvoice, name='create-invoice'),

]