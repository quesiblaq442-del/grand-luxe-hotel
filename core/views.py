from django.shortcuts import render # type: ignore

def home(request):
    """Render the home page."""
    return render(request, 'core/home.html')

def rooms(request):
  return render(request,'core/rooms.html')
def about(request):
  return render(request,'core/about.html')

def amenities(request):
  return render(request, 'core/amenities.html')