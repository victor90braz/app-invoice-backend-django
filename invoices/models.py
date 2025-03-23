from django.db import models

class Invoice(models.Model):
    number = models.CharField(max_length=50)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return f"Invoice {self.number} - {self.supplier}"
