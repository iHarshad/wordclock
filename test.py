import pyowm


owm = pyowm.OWM('42d3356ccc8eb2b64d2ac8acfffe0749')
observation = owm.weather_at_place("Ithaca,US")
w = observation.get_weather()
status = w.get_status
print(w.get_status())