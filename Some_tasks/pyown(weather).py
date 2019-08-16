import pyowm


def get_weather(city):
    """Function that returns the weather and temperature in certain city"""
    owm = pyowm.OWM('13d39c23d619e45499d67050af0598c3')
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')['temp']
    return 'In ' + city + ' the weather is ' + w.get_detailed_status() + '. ' + 'The temperature is ' +\
           str(temperature) + ' celsius.'


print(get_weather('Kyiv'))
