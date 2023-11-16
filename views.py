from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=513b51a6e200555aa6d3906cc9cc8e77'

    cities = City.objects.all()
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
    form = CityForm()
    
    weather_data = []

    for city in cities: #return all the cities in the database
     city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
     weatherapp = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
     }
    
    
     weather_data.append(weatherapp)
    context = {'weather_data' : weather_data,'form' : form}
    return render(request, 'wea.html',context) #returns the index.html template
    