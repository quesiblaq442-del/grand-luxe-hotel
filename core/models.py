from django.db import models

class Booking(models.Model):
  first_name =models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.CharField(max_length=20)
  check_in = models.DateField()
  check_out = models.DateField()
  guests = models.IntegerField(default=1)
  room_type = models.CharField(max_length=100)
  special_requests = models.TextField(max_length=500, blank=True)
  promo_code = models.CharField(max_length=50, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.first_name} {self.last_name} - {self.room_type} ({self.check_in} to {self.check_out})"
  
  class ContactInquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
      verbose_name_plural = "Contact Inquiries"
      
      def __str__(self):
        return f"{self.name} - {self.subject}"
      