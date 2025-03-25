# invoices/management/commands/seed_invoices.py

from django.core.management.base import BaseCommand
from django.db import connection
from invoices.factories import InvoiceFactory

class Command(BaseCommand):
    help = 'Truncates the Invoice table and seeds the database with 51 invoice objects'

    def handle(self, *args, **options):
        self.stdout.write('Truncating the invoices_invoice table...')
        with connection.cursor() as cursor:
            # RESTART IDENTITY resets the primary key counter back to 1
            # CASCADE is used if there are foreign key constraints on this table
            cursor.execute("TRUNCATE TABLE invoices_invoice RESTART IDENTITY CASCADE;")

        self.stdout.write('Seeding the invoices_invoice table with 51 invoices...')
        InvoiceFactory.create_batch(51)

        self.stdout.write(self.style.SUCCESS('Successfully truncated and created 51 invoices!'))
