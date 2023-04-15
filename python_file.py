				import requests

				# API key for OpenWeatherMap
				API_KEY = "725f72d3953a51c26fcddf41dceb5bde"

				# API endpoint for Toronto weather
				url = "http://api.openweathermap.org/data/2.5/weather?q=Toronto&appid=" + API_KEY

				# Get weather information for Toronto
				response = requests.get(url)
				data = response.json()

				# Get the temperature, weather description, and weather icon
				temp = data['main']['temp']
				weather_description = data['weather'][0]['description']
				weather_icon = data['weather'][0]['icon']

				cel=int(temp)-273

				ww_temp=(str(cel)+chr(176)+' C')
				ww_descript=weather_description.title()

				pyscript.write(temp)
				pyscript.write(weather_description)
