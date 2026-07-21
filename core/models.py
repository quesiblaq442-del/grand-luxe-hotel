from django.db import models
from django.utils import timezone

class Booking(models.Model):
  first_name =models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.CharField(max_length=20)
  check_in = models.DateField(default=timezone.now)
  check_out = models.DateField(null=True, blank=True)
  guests = models.IntegerField(default=1)
  room_type = models.CharField(max_length=100)
  special_requests = models.TextField(blank=True)
  promo_code = models.CharField(max_length=50, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.first_name} {self.last_name}"