from django.db import models
from django.conf import settings

# Create your models here.
class Transaction(models.Model):
    #Transaction id
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    #User who made the transaction
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    #mpesa receipt number
    mpesa_receipt_number = models.CharField(max_length=100, blank=True, null=True)
    #Transaction status
    status = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField( blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        print(f"Transaction-{self.mpesa_receipt_number} - {self.status} - {self.date_created}")
        return f"Transaction-{self.mpesa_receipt_number} - {self.status} - {self.date_created}"
# Create your models here.
