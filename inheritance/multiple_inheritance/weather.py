import requests
import settings

class Weather:
	root_url = settings.weather_root_url
	city_conecter = "?q="
	api_connecter = "&appid="

	def __init__(self, weather_token=None, city=None):
		self.weather_token = weather_token
		self.city = city

	def get_current_weather(self):
		url = f"{self.root_url}{self.city_conecter}{self.city}{self.api_connecter}{self.weather_token}"
		try:
			res = requests.get(url)
			weather_in_city = res.json()
			return weather_in_city
		except Exception:
			raise Exception(f"Something wrong with request: {res}")

"""
weather = Weather(weather_token=settings.weather_token, city="London")
weather_info =  weather.get_current_weather()
print(weather_info["weather"])
"""