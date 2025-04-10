import requests
import reverse_geocoder as rg
import pandas as pd

data = pd.read_csv('Registrations.csv')
df = pd.DataFrame(data=data)
print(df)
print('')
print('')

baseurl1 = 'https://api.airplanes.live/v2/reg/'			## API URL

def main_request(baseurl1, endpoint):					## Requests data from api
    r = requests.get(baseurl1 + endpoint)
    return r.json()										## Spits out json

def in_flight(response):								## Function to check whether in flight or not
    return response['total']

# def loc_lat(response):								## Function to check est. longitude (in case it is needed individually later on)
#     return response['ac'][0]['lat']
# 
# def loc_lon(response):								## Function to check est. latitude (in case it is needed individually later on)
#     return response['ac'][0]['lon']

def coords(response):									## Function to return coordinates from API
    lat = response['ac'][0]['lat']						## Latitude
    lon = response['ac'][0]['lon']						## Longitude
    strlat = str(lat)
    strlon = str(lon)
    horiz_latlon = (strlat + "," + strlon)
    return horiz_latlon

def geocode(response):									## Function to return reverse geocoded city, county, and state
    lat = response['ac'][0]['lat']						## Latitude
    lon = response['ac'][0]['lon']						## Longitude
    latlon = (lat, lon)
    geo = rg.search(latlon, mode=1)						## Reverse-geocoder module
    city = geo[0]['name']
    county = geo[0]['admin2']
    state = geo[0]['admin1']
    citycountystate = city + ", " + county + ", " + state 
    return citycountystate


df_reg_name = df['Registration ']
df_reg_agency = df['Agency']
df_reg_type = df['Type']
i = 0
for n in df_reg_name:
    data = main_request(baseurl1, n)					## Create variable with request function
    if in_flight(data) >= 1:							## Print location when flight is airborne
        print(n, df_reg_agency[i], df_reg_type[i])      ## Print Registration number and Agency
        i = i + 1
        ## print(loc_lat(data))							## Print latitude (in case it is needed individually later on)
        ## print(loc_lon(data))							## Print longitude (in case it is needed individually later on)
        print(coords(data))                             ## Print latitude and longitude
        print(geocode(data))                            ## Print city, neighborhood, county, state
        print('\n')
    else:
        print(n, df_reg_agency[i], df_reg_type[i])						## Print Registration number and Agency
        i = i + 1
        print('Not Airborne')                           ## Print not airborne if not in the air
        print('\n')
    
