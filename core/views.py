from django.shortcuts import render, redirect

from .models import Booking # type: ignore

def home(request):
    """Render the home page."""
    return render(request, 'core/home.html')

def rooms(request):
  return render(request,'core/rooms.html')

def about(request):
  return render(request,'core/about.html')

def amenities(request):
  return render(request, 'core/amenities.html')

def contact(request):
  return render(request, 'core/contact.html')

def booking(request):
  return render(request, 'core/booking.html')

def dinning(request):
  return render(request,'core/dinning.html')  

def gallery(request):
  return render(request,'core/gallery.html')

def offers(request):
  return render(request,'core/offers.html')

def booking(request):
  if request.method == 'POST':
    new_booking = Booking(
      first_name=request.POST.get('first_name', ''),
      last_name=request.POST.get('last_name', ''),
      email=request.POST.get('email', ''),
      phone=request.POST.get('phone', ''),
      check_in=request.POST.get('check_in'),
      check_out=request.POST.get('check_out'),
      guests=request.POST.get('guests'),
      room_type=request.POST.get('room_type', ''),
      special_requests=request.POST.get('special_requests'),
      promo_code=request.POST.get('promo_code', ''),
    )

    new_booking.save()
    return render(request, 'core/booking_success.html')
  return render(request, 'core/booking.html')