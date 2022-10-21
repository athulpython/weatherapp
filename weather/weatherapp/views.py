# import json to load json data to python dictionary
import json
import urllib

from django.shortcuts import render


# urllib.request to make a request to api

def index(request):
	if request.method == 'POST':
		city = request.POST['city']
		''' api key might be expired use your own api_key
			place api_key in place of appid ="your api key" '''

		source = urllib.request.urlopen(
		'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=your api key').read()

		list_of_data = json.loads(source)

		data = {
			'city' : city,
			"country_code": str(list_of_data['sys']['country']),
			'description' : (list_of_data)['weather'][0]['description'],
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']),
			"temp": str(list_of_data['main']['temp']) + 'k',
			"icon" : (list_of_data)['weather'][0]['icon'],
			"pressure": str(list_of_data['main']['pressure']),
			"humidity": str(list_of_data['main']['humidity']),
			"windspeed" : (list_of_data)['wind']['speed'],

		}
		print(data)
	else:
		data ={}
	return render(request, "main/index.html", data)
