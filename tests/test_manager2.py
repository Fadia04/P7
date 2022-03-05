import pytest
from classes.manager import Manager
from classes.parsers import Parser
from classes.wikiapi import Wiki_API
from classes.google_api import Google_API
import wikipedia
from classes.messages import positive_responses, negative_responses
from random import choice

class Test_Manager:
    """
    def mock_get_data(self):
        result = ["Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.", 'https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche']
        return result
   
    def mock_get_data_nok(self):
        result = []
        return result  
    
    def test_should_get_response(self, monkeypatch):
        
        manager = Manager("Où se trouve la tour eiffel?")
        monkeypatch.setattr('classes.wikiapi.Wiki_API.get_data', self.mock_get_data)
        
        assert manager.get_response() == {"status" : "ok",
                        "message" : choice(positive_responses),
                        "latitude" : 48.8421379, 
                        "longitude" :2.3219514,                        
                        "summary" : "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.", 
                        "url" : 'https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche'}
    
    def test_should_not_get_data(self, monkeypatch):
        manager = Manager(" Dis-moi, où se trouve la tour eiffel?")
        #monkeypatch.setattr('classes.wikiapi.Wiki_API.get_data', self.mock_get_data_nok)
        assert manager.get_response() == {"status": "nok",
                                           "message": choice(negative_responses) }
    
    
    
    
    def test_should_not_get_keyword(self, monkeypatch):
        manager = Manager(" Dis-moi, où se trouve?")        
    
        manager._get_keyword
        monkeypatch.setattr('classes.parsers.Parser.get_keyword', self.mock_get_keyword)
        assert manager.get_response() == {"status": "nok",
                                           "message": choice(negative_responses) }
    
    def mock_get_coordinates(self):
        if self.geocode_result: 
            lat = self.geocode_result[0]["geometry"]["location"]["lat"]
            lng = self.geocode_result[0]["geometry"]["location"]["lng"]
            return (lat, lng)
        else:
            return None 
   
    def mock_get_keyword_nok(self):
        result = " "
        return result           
    def test_should_not_get_coordinates(self, monkeypatch):
        manager = Manager("dis-moi où se?")
        #manager._get_coordinates
        #monkeypatch.setattr('classes.google_api.Google_API.get_coordinates', self.mock_get_keyword_nok)
        assert manager.get_response() == {"status": "nok",
                                           "message": choice(negative_responses) }"""
    
"""
class Test_Manager:
    def mock_geocode_ok(*args, **kwargs):
        result = [
            {"geometry": {"location": {"lat" : 1200, "lng": 3000}}}
        ]
        return result 

    def test_should_get_response(self, monkeypatch):
        manager = Google_API("tour eiffel")        
        monkeypatch.setattr('Google_API.get_coordinates()', self.mock_geocode_ok)
        manager= Google_API("Tour Eiffel Paris")
        
        assert manager.get_response() == {
                        
                        "status" : "nok"}"""

class Test_Manager:
    """
    def mock_get_keyword(self):
        result = "tour montparnasse"
        return result
    def mock_get_keyword_nok(self):
        result = " "
        return result

    def test_should_get_response(self, monkeypatch):
        parser = Manager(" Dis-moi, où se trouve la tour eiffel?")        

        monkeypatch.setattr('classes.parsers.Parser.get_keyword', self.mock_get_keyword)
        assert parser.get_response() == {"status" : "ok",
                        "message" : choice(positive_responses),
                        "latitude" : 48.8421379, 
                        "longitude" :2.3219514,                        
                        "summary" : "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.", 
                        "url" : 'https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche'}
    def test_should_not_get_response(self, monkeypatch):
        parser = Manager(" Dis-moi, où se trouve la tour eiffel?")        

        monkeypatch.setattr('classes.parsers.Parser.get_keyword', self.mock_get_keyword_nok)
        assert parser.get_response() == {"status" : "nok",
                                        "message" : choice(negative_responses)}
    
    def mock_get_data(self):
        result = ["Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.", 'https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche']
        return result
    def test_should_get_response2(self, monkeypatch):
        
        wikiapi = Manager(" Dis-moi, où se trouve la tour eiffel?")
        monkeypatch.setattr('classes.wikiapi.Wiki_API.get_data', self.mock_get_data)
        
        assert wikiapi.get_response() == {"status" : "ok",
                        "message" : choice(positive_responses),
                        "latitude" : 48.8421379, 
                        "longitude" :2.3219514,                        
                        "summary" : "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.", 
                        "url" : 'https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche'}
    """
    def mock_get_coordinates(self):  
        result = [
             {"lat" : 1200, "lng": 3000}
        ]
        return result                   
    def test_should_get_coodinates(self, monkeypatch):
        manager = Manager("coucou hhhh")        
        monkeypatch.setattr('classes.google_api.Google_API.get_coordinates', self.mock_get_coordinates)
        #manager= Google_API("Tour Eiffel Paris")
        
        assert manager.get_response() == (1200, 3000)
                        
                       