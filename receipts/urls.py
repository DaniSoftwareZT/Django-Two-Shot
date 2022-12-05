from django.urls import path
from receipts.views import receipt_list, create_receipt_view


urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt_view, name="create_receipt"),
]
#path("urlpath", view_function_name, name=url name)
