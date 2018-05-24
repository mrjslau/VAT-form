""" Models of 'vatforms' app """
from django.db import models
from django.contrib.auth.models import User

class Purchase(models.Model):
    """ Purchase class - details about products """
    productName = models.CharField(max_length=80)
    units = models.CharField(max_length=10)
    amount = models.IntegerField()
    price = models.FloatField()
    totalPrice = models.FloatField()

    def count_vat(self):
        return self.totalPrice * 0.21
    
    def count_sumwithvat(self):
        return self.totalPrice + self.totalPrice * 0.21

    def __str__(self):
        return self.productName

class VATInvoice(models.Model):
    """ VATInvoice class - a list of purchases with invoice attributes """
    series = models.CharField(max_length=5)
    seller = models.CharField(max_length=100)
    purchases = models.ManyToManyField(Purchase)
    totalSum = models.IntegerField()
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_enumpurchaseslist(self):
        return enumerate(list(self.purchases.all()), 1)

    # id series seller
    def __str__(self):
        return self.seller

class PurchasesWriteOffForm(models.Model):
    """ PurchasesForm class - form for accounting with purchases from invoices """
    institution = models.CharField(max_length=100)
    date = models.DateField
