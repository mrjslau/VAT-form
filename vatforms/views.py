""" Module for GET and POST HTTP requests to vatforms app """
import datetime
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
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
            return redirect('allinvoices')
        return render(request, 'vatforms/create.html',
                      {'error':'Visi laukai privalo būti užpildyti'})
    return render(request, 'vatforms/create.html')

def showinvoice(request, vatinvoice_id):
    """ Method to show one invoice with details """
    invoice = get_object_or_404(VATInvoice, pk=vatinvoice_id)
    return render(request, 'invoices/show.html', {'invoice':invoice})

def allinvoices(request):
    """ Method to show all invoices """
    invoices = get_list_or_404(VATInvoice)
    return render(request, 'invoices/all.html', {'invoices':invoices})