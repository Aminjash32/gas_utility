from django.db import models

# Create your models here.
# service_request/models.py
from django.db import models
from customer.models import Customer

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('GAS_LEAK', 'Gas Leak'),
        ('BILLING_ISSUE', 'Billing Issue'),
        ('MAINTENANCE', 'Maintenance'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request {self.id} - {self.status}"
