from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
def home(request):
    featured_cars = Car.objects.order_by('created_data').filter(is_featured = True)
    all_cars = Car.objects.order_by('created_data')
    teams = Team.objects.all()
    data = {
        'teams' : teams,
        'featured_cars':featured_cars,
        'all_cars' : all_cars,
        }
    return render(request,'pages/home.html',data)
def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
        }
    return render(request,'pages/about.html',data)
def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')