from django.shortcuts import render, HttpResponse
from django.contrib import messages
import requests
import  datetime

# Create your views here.
# e6beade53c6d5ace90561bc09813eb51
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def home(request):
    print(request.POST)

#     <script async src="https://cse.google.com/cse.js?cx=f71d271d48ee348c4">
# </script>
# <div class="gcse-search"></div>

    custom_json_search_key = 'AIzaSyBiA_4VDshEDpOZ6xXczLkNNuww-i0juSM'
    if 'city' in request.POST:
  
      city = request.POST['city']
    else:
      city = 'indore'   
    # API URL and parameters
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': 'e6beade53c6d5ace90561bc09813eb51',  # Replace with your API key
        'units': 'metric',
      }

    try:
       response = requests.get(url, params = params)
       response.raise_for_status()  # Raise an exception for HTTP errors
       data = response.json()
       description = data['weather'][0]['description']
       icon = data['weather'][0]['icon']
       temp = data['main']['temp']
     
    
  
       day  = datetime.date.today()

    except requests.exceptions.RequestException as e:
                # Handle API request errors
        error_message = f"Error fetching weather data: {e}"
        messages.error(request,error_message)
        return render(request, 'index.html', {'description':description,'icon':icon, 'temp':temp, 'day':day, 'city':city})
    except KeyError:
        # Handle invalid API response (e.g., city not found)
        error_message = "City not found. Please try again."

        return render(request,'index.html',{'error':error_message})
    print('This is city: ' + city + ', description: '+ description)

    return render(request,'index.html',{'description':description,'icon':icon, 'temp':temp, 'day':day, 'city':city})
 
    



 
