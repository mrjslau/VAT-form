""" Module for GET and POST HTTP requests to vatforms app """
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import VATInvoice

def home(request):
    """ Method to display homepage """
    return render(request, 'vatforms/home.html')

@login_required
def createinvoice(request):
    """ Method to create empty vatinvoice """
    if request.method == 'POST':
        if request.POST['series'] and request.POST['seller']:
            vatinvoice = VATInvoice()
            vatinvoice.series = request.POST['series']
            vatinvoice.seller = request.POST['seller']
            vatinvoice.totalSum = 0
            vatinvoice.date = datetime.date.today()
            vatinvoice.owner = request.user
            vatinvoice.save()
            return redirect('home')
        return render(request, 'vatforms/create.html',
                      {'error':'Visi laukai privalo būti užpildyti'})
    return render(request, 'vatforms/create.html')
