from django.urls import path
from receipts.views import receipt_list, create_receipt_view, category_list, account_list, create_category


urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt_view, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
    path("categories/create/", create_category, name="create_category"),
]
#path("urlpath", view_function_name, name=url name)
