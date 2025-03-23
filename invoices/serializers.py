from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField()

    class Meta:
        model = Invoice
        fields = '__all__'
