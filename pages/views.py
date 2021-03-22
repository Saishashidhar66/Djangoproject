from django.shortcuts import render
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
# Create your views here.
def home(request):
    featured_cars = Car.objects.order_by('created_data').filter(is_featured = True)
    all_cars = Car.objects.order_by('created_data')
    teams = Team.objects.all()
    #search_fields= Car.objects.values('model','state','year','body_style')
    
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



