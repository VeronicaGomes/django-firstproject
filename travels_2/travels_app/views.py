from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination,Hotel
# Create your views here.

def index(request):

	dests = Destination.objects.all()
	return render(request,'travels_app/index.html', {'dests': dests})
	
	
def hotel(request):

	places = Hotel.objects.all()
	return render(request,'travels_app/hotel.html', {'places': places})
		

def hoteltickets(request):

	places = Hotel.objects.all()
	return render(request,'travels_app/hoteltickets.html', {'places': places})


def airplanetickets(request):

	dests = Destination.objects.all()
	return render(request,'travels_app/airplanetickets.html' , {'dests': dests})	

