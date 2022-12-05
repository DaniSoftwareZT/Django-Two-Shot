from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipt
from django.contrib.auth.decorators import login_required
from .forms import CreateViewForm

# Create your views here.


@login_required
def receipt_list(request):
    receipt_list = Receipt.objects.filter(purchaser = request.user)
    context = {
        "receipt_list": receipt_list #connected to line 8
    }
    #use the context dictionary key "" to access receipt_list in templates
    return render(request, "receipts/list.html", context) #pass context to render function

#this @ = you have to be logged in to access it
@login_required
def create_receipt_view(request):
    if request.method == "POST":
        form = CreateViewForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = CreateViewForm()

    context = {
        "form": form
}

    return render(request, "receipts/create.html", context)
