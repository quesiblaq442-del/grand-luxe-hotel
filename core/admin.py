from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'email', 'phone', 'check_in', 'check_out', 'room_type', 'created_at')
  list_filter = ('check_in', 'room_type')
search_fields = ('first_name', 'last_name', 'email')