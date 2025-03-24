from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Invoice
from .serializers import InvoiceSerializer

@api_view(['GET'])
def invoice_list(request: Request) -> Response:
    invoices = Invoice.objects.order_by('id')
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)
