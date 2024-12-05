from djongo import models
from django.utils import timezone

class Recibo(models.Model):
    user = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    description = models.TextField(blank=True, null=True)  # Descripción opcional del pago
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer')], default='credit_card')  # Método de pago
    receipt_number = models.CharField(max_length=50, unique=True)  # Número de recibo único

    def __str__(self):
        return f"Recibo {self.transaction_id} - {self.status}"
