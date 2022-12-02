from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipt

# Create your views here.


def receipt_list(request):
    receipt_list = Receipt.objects.all()
    context = {
        "receipt_list": receipt_list #connected to line 8
    }
    #use the context dictionary key "" to access receipt_list in templates
    return render(request, "receipts/list.html", context) #pass context to render function
