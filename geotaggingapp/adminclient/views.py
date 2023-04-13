# Create your views here.

from django.shortcuts import render, HttpResponse
import requests

# THIS IS OUR API KEY DO NOT LOSE IT
# if we lose it i can just go get it again but yea
# for good measure here it is again
# 69085a26250343e6bb8936995e02e4c3-
api_key = '69085a26250343e6bb8936995e02e4c3';

api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key


def get_ip_geolocation_data(ip_address):    

    response = requests.get(api_url) 
    # okay we got the longitude latitude information but its not showing in
    # the app instead its printed in the terminal
    # so ig we just have to parse this

    print(response.content)



def adminclientview(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    get_ip_geolocation_data(ip)
  

    return HttpResponse("Welcome! You are visiting from: {}".format(ip))