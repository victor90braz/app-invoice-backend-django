from django.contrib import admin
from django.urls import path

from invoices.views import invoice_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoices/', invoice_list, name='invoice-list'),
]
