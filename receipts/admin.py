from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt
# Register your models here.


class ExpenseCategoryAdmin(admin.ModelAdmin):
    admin.site.register(ExpenseCategory)


class AccountAdmin(admin.ModelAdmin):
    admin.site.register(Account)


class ReceiptAdmin(admin.ModelAdmin):
    admin.site.register(Receipt)
