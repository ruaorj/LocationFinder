import requests
import pyfiglet

ascii_art = pyfiglet.figlet_format("Location Finder" , font='slant')
print(ascii_art)

api_key = '118a0e808c254602be00f478f890e49f'
ip = input("Enter an IP: ")

print("--------------------------------------------------")

url = f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}'

response = requests.get(url)

data = response.json()

print(f"IP: {data.get('ip')}")
print(f"City: {data.get('city')}")
print(f"State: {data.get('state_prov')}")
print(f"Country: {data.get('country_name')}")
print(f"Latitude: {data.get('latitude')}")
print(f"Longitude: {data.get('longitude')}")
print(f"Calling code: {data.get('calling_code')}")
print(f"Country emoji: {data.get('country_emoji')}")
print(f"ISP: {data.get('organization')}")

timezone = data.get('time_zone')
if timezone:
    current_time = timezone.get('current_time')
    if current_time:
        print(f"Current time: {current_time}")
    else:
        print("Current time info not available.")
else:
    print("Timezone info not available.")
