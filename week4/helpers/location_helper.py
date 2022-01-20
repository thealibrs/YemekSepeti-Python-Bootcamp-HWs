from geopy.geocoders import Nominatim
from constants.messages import CustomMessages

class LocationHelper:

    def getLocation(self, latitude, longitude):
        try:
            geoLoc = Nominatim(user_agent="GetLoc")
            locname = geoLoc.reverse(f"{latitude}, {longitude}")
            country = str(locname.address).split()[-1]
            
            return country
            
        except:
            print(CustomMessages.LOCATION_ERROR)



