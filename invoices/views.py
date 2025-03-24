from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from .models import Invoice
from .serializers import InvoiceSerializer

@api_view(['GET'])
def invoice_list(request: Request) -> Response:
    invoices = Invoice.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(invoices, request)

    serializer = InvoiceSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
