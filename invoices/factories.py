import factory
from .models import Invoice
from datetime import date
import random

class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice

    number = factory.Sequence(lambda n: f"INV-{n+1000}")
    date = factory.LazyFunction(date.today)
    amount = factory.LazyFunction(lambda: round(random.uniform(100, 1000), 2))
    supplier = factory.Faker('company')
