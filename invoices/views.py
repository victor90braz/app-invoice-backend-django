from django.http import JsonResponse
from .models import Invoice

def invoice_list(request):
    invoices = Invoice.objects.all().values()
    return JsonResponse(list(invoices), safe=False)
