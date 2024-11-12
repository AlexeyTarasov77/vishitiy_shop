from django.db import models

# Create your models here.


class Payment(models.Model):
    order_id = models.CharField(max_length=255)
    order_desc = models.CharField(max_length=255)
    currency = models.CharField(max_length=3, default="UAH")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    signature = models.CharField(max_length=255)
    merchant_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="created")
    payment_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_id
