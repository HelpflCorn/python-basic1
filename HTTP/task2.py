import requests

def weather(city_name, access_key):
    params = {'access_key': access_key, 'query': city_name, 'units' : 'm'}
    api_result = requests.get('https://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return api_response

print(weather("Kyiv", "fd7178a2abda4e9b1289cc7141187060")) #my key gives error 105 due to free profile limitations :(

