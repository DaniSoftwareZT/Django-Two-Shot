from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipt, Account, ExpenseCategory
from django.contrib.auth.decorators import login_required
from .forms import CreateViewForm, ExpenseCategoryForm, AccountForm

# Create your views here.


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST) #connected to line 20
        if form.is_valid():
            accounts = form.save(commit=False)
            accounts.owner = request.user
            accounts.save()
            return redirect("account_list")
    else:
        form = AccountForm()
    context = {"form": form}
    return render(request, "accounts/create.html", context)



@login_required
def create_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST) #connected to line 36
        if form.is_valid():
            categories = form.save(commit=False)
            categories.owner = request.user
            categories.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm()
    context = {"form": form}
    return render(request, "expenses/create.html", context)


@login_required
def category_list(request):
    category_list = ExpenseCategory.objects.filter(owner=request.user)
    context = {"category_list": category_list}
    return render(request, "receipts/list.html", context)


@login_required
def account_list(request):
    account_list = Account.objects.filter(owner=request.user)
    context = {"account_list": account_list}
    return render(request, "accounts/list.html", context)


@login_required
def receipt_list(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {"receipt_list": receipt_list}  # connected to line 8
    # use the context dictionary key "" to access receipt_list in templates
    return render(
        request, "receipts/list.html", context
    )  # pass context to render function


# this @ = you have to be logged in to access it
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

    context = {"form": form}

    return render(request, "receipts/create.html", context)
