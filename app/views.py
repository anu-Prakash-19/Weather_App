from django.shortcuts import render
import requests

def index(request):
    city = request.GET.get('city', 'bangalore')
    api_key = '5a73b4ef8cb956cdc3c2af29395e759f'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    temperature = None
    country = None
    error_message = None

    try:
        api_response = requests.get(api_url).json()
        
        # Check if API returned valid data
        if api_response.get("cod") == 200:
            temperature = api_response['main']['temp']
            city = api_response['name']
            country = api_response['sys']['country']
        else:
            error_message = api_response.get("message", "Unable to fetch weather data.")
    
    except Exception as e:
        error_message = str(e)

    return render(request, 'index.html', {
        'temperature': temperature,
        'city': city,
        'country': country,
        'error': error_message
    })
