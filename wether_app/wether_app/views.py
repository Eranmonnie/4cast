from django.shortcuts import render
import json 
import urllib.request


def home(request):
    if request.method =='POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=61f2c51a882bf28071916befdca76cc6').read()
        json_data = json.loads(res)

        data = {
            'Country' : str(json_data['sys']['country']),

            'Coordinate' : str(json_data['coord']['lon'])+' '+ 
            str(json_data['coord']['lat']),

            'Temperature' : str(json_data['main']['temp'])+'k',

            'Pressure' : str(json_data['main']['pressure']),

            'Humidity' : str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}
    return render(request, 'home.html', {'city':city,'data':data} )