from __future__ import unicode_literals
from .models import *
from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    received_data=coordinates.objects.all()[len(coordinates.objects.all())-1]
    lat=str(received_data.lat)
    lon=str(received_data.lon)
    speed=str(received_data.speed)
    x=str(received_data.x)
    y=str(received_data.y)
    z=str(received_data.z)
    ultra=str(received_data.ultra)
    smoke=str(received_data.smoke)
    heart=str(received_data.heart)
    context={'a':lat,'b':lon,'c':speed,'d':x,'e':y,'f':z,'g':ultra,'h':smoke,'i':heart}
    return render(request,'accident_avoidance/index.html',context)
def getdata(request):
    if request.method=='GET' :
        lat_value=request.GET['lat']
	lon_value=request.GET['lon']
	speed_value=request.GET['speed']
	heart_value=request.GET['heart']
	x_value=request.GET['x']
	y_value=request.GET['y']
	z_value=request.GET['z']
	ultra_value=request.GET['ultra']
	smoke_value=request.GET['smoke']
	#c = coordinates.objects.create(lat=lat_value,lon=lon_value)
	c = coordinates.objects.create(lat=lat_value,lon=lon_value,speed=speed_value,heart=heart_value,x=x_value,y=y_value,z=z_value,ultra=ultra_value,smoke=smoke_value)
        c.save()
        return HttpResponse("data saved in db")
    else:
        #Otherwise it will return error
	return HttpResponse("error")

def pulse(request):
	received_data1=coordinates.objects.all()[len(coordinates.objects.all())-1]
	received_data2=coordinates.objects.all()[len(coordinates.objects.all())-2]
	received_data3=coordinates.objects.all()[len(coordinates.objects.all())-3]
	received_data4=coordinates.objects.all()[len(coordinates.objects.all())-4]
	received_data5=coordinates.objects.all()[len(coordinates.objects.all())-5]
	received_data6=coordinates.objects.all()[len(coordinates.objects.all())-6]
	received_data7=coordinates.objects.all()[len(coordinates.objects.all())-7]
	heart1=str(received_data1.heart)
	heart2=str(received_data2.heart)
	heart3=str(received_data3.heart)
	heart4=str(received_data4.heart)
	heart5=str(received_data5.heart)
	heart6=str(received_data6.heart)
	heart7=str(received_data7.heart)			
				
	context={'a1':heart1,'a2':heart2,'a3':heart3,'a4':heart4,'a5':heart5,'a6':heart6,'a7':heart7}	
	return render(request,'accident_avoidance/pulse.html',context)
    
'''def accelerometer(request):
	
	received_data=coordinates.objects.all()[len(coordinates.objects.all())-1]
				
				
	context={'received_data':received_data}	
	return render(request,'accident_avoidance/accelerometer.html',context)
def ult(request):
	
	received_data=coordinates.objects.all()[len(coordinates.objects.all())-1]
				
				
	context={'received_data':received_data}	
	return render(request,'accident_avoidance/ult.html',context)
'''
