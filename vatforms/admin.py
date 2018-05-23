from django.contrib import admin
from .models import Purchase, VATInvoice, PurchasesForm

admin.site.register(Purchase)
admin.site.register(VATInvoice)
admin.site.register(PurchasesForm)