from django.urls import path
from receipts.views import receipt_list


urlpatterns = [
    path("", receipt_list, name="home"),
]
#path("urlpath", view_function_name, name=url name)
