import requests
import reverse_geocoder as rg

## List of registration numbers and dictionary listing agency and whether reg is a plane or helicopter
reg_list = ['N982HP', 'N978HP', 'N153HP', 'N202HP', 'N979HP', 'N137HP', 'N974HP', 'N976HP', 'N511HP', 'N159HP']
reg_dict = {'N982HP':'CHP Helicopter', 'N978HP':'CHP Helicopter', 'N153HP':'CHP Plane', 'N202HP':'CHP Plane', 'N979HP':'CHP Helicopter', 'N137HP':'CHP Plane', 'N974HP':'CHP Helicopter', 'N976HP':'CHP Helicopter', 'N511HP':'CHP Plane', 'N159HP':'CHP Plane'}

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


for n in reg_list:
    i = 0
    data = main_request(baseurl1, n)					## Create variable with request function
    if in_flight(data) >= 1:							## Print location when flight is airborne
        print(n, reg_dict[n])
        ## print(loc_lat(data))							## Print latitude (in case it is needed individually later on)
        ## print(loc_lon(data))							## Print longitude (in case it is needed individually later on)
        print(coords(data))
        print(geocode(data))
        print('\n')
        i + 1
    else:
        print(n, reg_dict[n])							## Print not airborne if not in the air
        print('Not Airborne')
        print('\n')

    
    