from django.contrib import admin
from .models import Booking, ContactInquiry

admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'email', 'phone', 'check_in', 'check_out', 'room_type', 'created_at')
  list_filter = ('check_in', 'check_out', 'room_type')
  search_fields = ('first_name', 'last_name', 'email')
  
  @admin.register(ContactInquiry)
  class ContactInqiry(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'subject' , 'created_at')
    list_filter = ('created_at')
    search_fields = ('name', 'email', 'subject')