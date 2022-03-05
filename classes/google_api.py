import googlemaps


class Google_API:
    def __init__(self, keyword):

        gmaps = googlemaps.Client(key="AIzaSyCGNSkOgIZ34i2OQ3-asFcMnntaUbfQFIg")
        self.geocode_result = gmaps.geocode(keyword)

    def get_coordinates(self):

        if self.geocode_result:
            # return (self.geocode_result[0]["geometry"]["location"])
            # address = self.geocode_result[0]["formatted_address"]
            lat = self.geocode_result[0]["geometry"]["location"]["lat"]
            lng = self.geocode_result[0]["geometry"]["location"]["lng"]
            print(self.geocode_result[0])
            return (lat, lng)
        else:
            return None


"""
a = Google_API("Tour Montparnasse paris")
a.get_coordinates()
print(a.get_coordinates())"""
