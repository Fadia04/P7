import wikipedia


class Wiki_API:
    """This class uses the coordinates obtained by Google_API class to make requests to Wikipedia
    and get informations of the place asked by the user
    """

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_data(self):
        """This function set the langage in french and uses geosearch method to return a list containing a summary and an url
        if the page_title of the place asked is found. If page_title is not avalable, it returns None
        """
        wikipedia.set_lang("fr")
        geosearch = wikipedia.geosearch(self.latitude, self.longitude)
        if geosearch:
            page_title = geosearch[0]

            if page_title:
                self.link = wikipedia.page(page_title)
                url = self.link.url
                summary = self.link.summary

                return (summary, url)
            else:
                return None
        else:
            return None
