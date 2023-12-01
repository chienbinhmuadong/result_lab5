import requests 
API_KEY='b7a21354ab464ff233aeb13939fb9582'

class WeatherAPI:
    base_url='http://api.openweathermap.org'
    url_coord='/geo/1.0/direct'
    url_weather='/data/2.5/weather'
    def __init__(self, city='Saint-Petersburg', country='Russia', lg='ru'):
        self.city=city
        self.country=country
        self.lg=lg
        self.lat=0
        self.lon=0
        

    def retrieve_coord(self):
        params={'q': f'{self.city},{self.country}',
                'limit':1,
                'appid':API_KEY}
        url=f'{self.base_url}{self.url_coord}'
        response=requests.get(url, params=params)
        data=response.json()
        #print(response.status_code, response.reason)
        self.lat=data[0]['lat']
        self.lon=data[0]['lon']
        

    def analiz_weather(self):
        params={'lat': self.lat,
                'lon': self.lon,
                'units':'metric',
                'cnt': 1,
                'lang': self.lg,
                'appid': API_KEY}
        url= f'{self.base_url}{self.url_weather}'
        response= requests.get(url,params=params)
        data=response.json()
        temp=data['main']['temp']
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        print(f'город: {self.city}\n-погода: {temp}°C\n-влажность: {humidity}%\n-давление: {pressure}')


if __name__=='__main__':
   weather=WeatherAPI(city='Moscow', country='Russia')
   weather.retrieve_coord()
   weather.analiz_weather()