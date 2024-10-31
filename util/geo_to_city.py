import requests
import json

google_maps_api_key = "ADD KEY HERE"


def geo_to_city ( geo_string ):
    if 'POINT (' in geo_string:
        new_str = geo_string.replace ( 'POINT (', '')
        new_str = new_str.replace ( ')', '' )
        
        geo_split = new_str.split ( ' ' )
        longitude = geo_split[0]
        latitude = geo_split[1]
        print ( f'lat: {latitude}' )
        print ( f'lon: {longitude}' )
        city = new_str
        
        #Look up city and state
        google_maps_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + latitude + ',' + longitude + '&key=' + google_maps_api_key
        response = requests.get ( google_maps_url )
        result = response.json ()
        print ( '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' )
        #print ( json.dumps ( result, indent = 4 ) )
        plus_code = result['plus_code']
        if plus_code.get ( 'compound_code' ) is not None:
            compound_code = plus_code['compound_code']
            result_split = compound_code.split ( ' ', 1 )
            city_state = result_split[1]
            temp = city_state.split ( ',' )
            res = ','.join ( temp[:2] ), ','.join ( temp[2:] )
            city_state = res[0].split ( ',' )
            city = city_state[0]
            state = city_state[1]

            #Set tuple
            return_value = (city, state)
        else:
            return_value = ( 'UNAVAILABLE', 'UNAVAILABLE' )
    else:
        return_value = ( 'UNAVAILABLE', 'UNAVAILABLE' )
    
    print ( f'result: {return_value}' )
    
    return return_value



if __name__ == "__main__":
    test_data = ["POINT (-107.55145 42.999627)", "POINT (-74.655514 40.110253)",
                 "POINT (-71.481104 42.151077)", "POINT (-86.2818 39.919991)"]
    
    for item in test_data:
        geo_to_city ( item )