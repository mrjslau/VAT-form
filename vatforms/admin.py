from django.contrib import admin
from .models import Purchase, VATInvoice, PurchasesWriteOffForm

admin.site.register(Purchase)
admin.site.register(VATInvoice)
admin.site.register(PurchasesWriteOffForm)
