from django.db import models

# Create your models here.
# support/models.py
from django.contrib.auth.models import User
from django.db import models

class SupportRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    support_area = models.CharField(max_length=50)  # e.g., 'Billing', 'Technical Support'

    def __str__(self):
        return f"{self.user.username} - {self.support_area}"
