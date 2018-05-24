from django.urls import path
from . import views

urlpatterns = [
    path('create-invoice', views.createinvoice, name='create-invoice'),
    path('invoices/<int:vatinvoice_id>', views.showinvoice, name='showinvoice'),
    path('invoices/all', views.allinvoices, name='allinvoices'),

]