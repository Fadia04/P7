<<<<<<< HEAD
import pytest
from classes.manager import Manager
from classes.parsers import Parser
from classes.wikiapi import Wiki_API
from classes.google_api import Google_API
import wikipedia



=======
from classes.manager import Manager


class MockResponseOk:
    @staticmethod
    def geocode(keyword):
        result = [{"geometry": {"location": {"lat": 1200, "lng": 3000}}}]
        return result
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d


class Test_Manager:
    def mock_get_keyword(*args, **kwargs):
        result = "tour montparnasse"
        return result

    def mock_get_keyword_nok(*args, **kwargs):
        result = None
        return result

    def mock_get_coordinates(*args, **kwargs):
        result = (48.8421379, 2.3219514)
        return result

    def mock_get_coordinates_nok(*args, **kwargs):
        result = None
        return result

    def mock_get_data(*args, **kwargs):
        result = (
            "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.",
<<<<<<< HEAD
            "https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche"
        )
        return result
    
=======
            "https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche",
        )
        return result
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d

    def mock_get_data_nok(*args, **kwargs):
        result = None
        return result

<<<<<<< HEAD
    def test_should_not_get_keyword(self, monkeypatch):
        parser = Manager("Dis-moi, où se trouve la tour eiffel?")
        monkeypatch.setattr(
            "classes.parsers.Parser.get_keyword", self.mock_get_keyword
=======
    def mock_google(*args, **kwargs):
        return MockResponseOk()

    def test_should_not_get_keyword(self, monkeypatch):
        parser = Manager("Dis-moi, où se trouve la tour eiffel?")
        monkeypatch.setattr(
            "classes.parsers.Parser.get_keyword", self.mock_get_keyword_nok
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d
        )
        assert parser.get_response()["status"] == "nok"

    def test_should_not_get_coordinates(self, monkeypatch):
        gapi = Manager("Dis-moi, où se trouve la tour eiffel?")
        monkeypatch.setattr("classes.parsers.Parser.get_keyword", self.mock_get_keyword)
<<<<<<< HEAD
        monkeypatch.setattr("classes.parsers.Parser.get_keyword",self.mock_get_coordinates_nok)
        assert gapi.get_response()["status"] == "nok"


    def test_should_not_get_data(self, monkeypatch):
        wikiapi = Manager("Dis-moi, où se trouve la tour eiffel?")
        monkeypatch.setattr("classes.parsers.Parser.get_keyword", self.mock_get_keyword)
        monkeypatch.setattr(
            "classes.google_api.Google_API.get_coordinates", self.mock_get_coordinates
        )
        monkeypatch.setattr("classes.parsers.Parser.get_keyword", self.mock_get_data_nok)
=======
        monkeypatch.setattr("googlemaps.Client", self.mock_google)
        monkeypatch.setattr(
            "classes.google_api.Google_API.get_coordinates", self.mock_get_coordinates_nok
        )
        assert gapi.get_response()["status"] == "nok"

    def test_should_not_get_data(self, monkeypatch):
        wikiapi = Manager("Dis-moi, où se trouve la tour eiffel?")
        monkeypatch.setattr("classes.parsers.Parser.get_keyword", self.mock_get_keyword)
        monkeypatch.setattr("googlemaps.Client", self.mock_google)
        monkeypatch.setattr(
            "classes.google_api.Google_API.get_coordinates", self.mock_get_coordinates
        )
        monkeypatch.setattr(
            "classes.wikiapi.Wiki_API.get_data", self.mock_get_data_nok
        )
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d
        assert wikiapi.get_response()["status"] == "nok"

    def test_should_get_response(self, monkeypatch):
        manager = Manager("Dis-moi, où se trouve la tour eiffel?")
        monkeypatch.setattr("classes.parsers.Parser.get_keyword", self.mock_get_keyword)
<<<<<<< HEAD
        monkeypatch.setattr("classes.parsers.Parser.get_keyword", self.mock_get_coordinates)
        monkeypatch.setattr("classes.parsers.Parser.get_keyword", self.mock_get_data)
        
=======
        monkeypatch.setattr("googlemaps.Client", self.mock_google)
        monkeypatch.setattr(
            "classes.google_api.Google_API.get_coordinates", self.mock_get_coordinates
        )
        monkeypatch.setattr("classes.wikiapi.Wiki_API.get_data", self.mock_get_data)

>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d
        assert manager.get_response()["status"] == "ok"
        assert manager.get_response()["latitude"] == 48.8421379
        assert manager.get_response()["longitude"] == 2.3219514
        assert (
            manager.get_response()["summary"]
<<<<<<< HEAD
            == "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse."
=======
            == ("Montparnasse Rive Gauche  est un centre commercial français situé "
                "dans le quartier Necker du 15e arrondissement de Paris. Situé au "
                "pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier "
                "Tour Maine-Montparnasse. Il accueillait notamment les Galeries "
                "Lafayette Montparnasse.")
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d
        )
        assert (
            manager.get_response()["url"]
            == "https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche"
        )
<<<<<<< HEAD
"""
class MockResponse:
    @ staticmethod
    def get_keyword():
        return "tour montparnasse"
    #@ staticmethod
    #def get_coordinates(keyword):
        #return (1300, 3500)
    def get_data(lat, lng):
        return ("Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.", 'https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche')

class TestManager:
    def mock_get_keyword(*args, **kwargs):
        return MockResponse
    #def mock_get_coordinates(*args, **kwargs):
        #return MockResponse
    def mock_get_data(*args, **kwargs):
        return MockResponse

    def test_should_get_response(self, monkeypatch):
        manager = Manager("Dis-moi, où se trouve la tour eiffel?")
        monkeypatch.setattr("classes.parsers.Parser.get_keyword", self.mock_get_keyword)
        #monkeypatch.setattr(
           # "classes.google_api.Google_API.get_coordinates", self.mock_get_coordinates
        #)
        monkeypatch.setattr("classes.wikiapi.Wiki_API.get_data", self.mock_get_data)
        
        assert manager.get_response()["status"] == "ok"
        assert manager.get_response()["latitude"] == 1300
        assert manager.get_response()["longitude"] == 3500
        assert (
            manager.get_response()["summary"]
            == "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse."
        )
        assert (
            manager.get_response()["url"]
            == "https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche"
        )"""

    
    
    
    
   
    
    
       
=======
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d
