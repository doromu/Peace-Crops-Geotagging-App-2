from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from django.conf import settings
from qrcode import *
import requests
import json

# THIS IS OUR API KEY DO NOT LOSE IT
# if we lose it i can just go get it again but yea
# for good measure here it is again
# 69085a26250343e6bb8936995e02e4c3-
api_key = '69085a26250343e6bb8936995e02e4c3';

api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key

long = ""
lat = ""
ip = ""

def get_ip_geolocation_data(ip_address, long, lat):    
    
    response = requests.get(api_url) 
    # okay we got the longitude latitude information but its not showing in
    # the app instead its printed in the terminal
    # so ig we just have to parse this

    stack = response.content
    data = json.loads(stack)
    long = data['longitude']
    lat = data['latitude']
    
    return long, lat


data=None
def qr_gen(request):
    global data
    
    if request.method=="POST":
        ip = request.POST['data']
        data=request.POST['data']
        img=make(data)
        img.save("static/image/test.png")
    else:
        pass
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    getCoords = get_ip_geolocation_data(ip, long, lat)
    x = getCoords[0]
    y = getCoords[1]
        
    print(x)
    print(y)
        
    context = {
        'long' : x,
        'lat' : y,
        'data' : data,
    }
    
    return render(request,"index.html", context)

def adminclientview(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    get_ip_geolocation_data(ip, long, lat)
  

    return HttpResponse("Welcome! You are visiting from: {}".format(ip))

def index(request):
    return render(request,'index.html')