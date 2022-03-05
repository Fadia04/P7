import googlemaps

import os


class Google_API:
    """This class uses the keyword obtained from class Parser to make requests
    to Google API and get the coordinates of the place asked by the user
    """

    def __init__(self, keyword):
        """Init function to create googlemaps client"""
        google_api_key = os.getenv("GOOGLE_SECRET_KEY")
        gmaps = googlemaps.Client(key=google_api_key)
        self.geocode_result = gmaps.geocode(keyword)

    def get_coordinates(self):
        """This function returns a dictionnary containing the latitude
        and the longitude when there is a geocode result otherwise, it returns None
        """

        if self.geocode_result:
            lat = self.geocode_result[0]["geometry"]["location"]["lat"]
            lng = self.geocode_result[0]["geometry"]["location"]["lng"]
            print(self.geocode_result[0])
            return (lat, lng)
        else:
            return None
