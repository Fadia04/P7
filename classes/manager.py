from classes.parsers import Parser
from classes.google_api import Google_API
from classes.wikiapi import Wiki_API
from classes.messages import positive_responses, negative_responses
from random import choice


class Manager:
    """This class manages Parse, Google_API and Wiki_API classes and uses
    private functions to get the final response
    witch will be sended to the front end
    """

    def __init__(self, question):
        """The init function initialise the Parser"""
        self.parser = Parser(question)

    def get_response(self):
        """This function uses the keyword if exists, the coordinates if exist and the
        wikipedia data if exist to returns a dictionnary containg the status: ok or not ok,
        a positive or negative response choosen randomly
        from the messages file, the coordinates and the summary and url of the place wanted by the user
        """
        keyword = self._get_keyword()

        if keyword:
            coordinates = self._get_coordinates(keyword)

            if coordinates:
                wiki_data = self._get_data(coordinates[0], coordinates[1])

        if keyword and coordinates and wiki_data:
            response = {
                "status": "ok",
                "message": choice(positive_responses),
                "latitude": coordinates[0],
                "longitude": coordinates[1],
                "summary": wiki_data[0],
                "url": wiki_data[1],
            }
        else:
            response = {"status": "nok", "message": choice(negative_responses)}
        return response

    def _get_keyword(self):
        self.parser.parse()
        keywords = self.parser.get_keyword()
        return keywords

    def _get_coordinates(self, keywords):
        googleApi = Google_API(keywords)
        coordinates = googleApi.get_coordinates()
        return coordinates

    def _get_data(self, lat, lng):
        wiki_api = Wiki_API(lat, lng)
        response = wiki_api.get_data()
        if response is not None:
            return response
        else:
            return None
