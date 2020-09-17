from django.conf.urls import url
from travels_app import views

app_name ='travels_app'

urlpatterns = [
    url(r'^hotel/$',views.hotel,name='hotel'),
    url(r'^hoteltickets/$',views.hoteltickets,name='hoteltickets'),
    url(r'^airplanetickets/$',views.airplanetickets,name='airplanetickets'),

]