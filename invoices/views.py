from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from .models import Invoice
from .serializers import InvoiceSerializer

@api_view(['GET'])
def invoice_list(request: Request) -> Response:
    invoices = Invoice.objects.order_by('id')

    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(invoices, request)

    if page is not None:
        serializer = InvoiceSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)
