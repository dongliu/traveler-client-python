import logging
from traveler_client import traveler, client


def test_create():
    form_id = '5fe6817cfb700100129f0231'
    traveler_client = traveler.Traveler('https://localhost:3443', 'api_write', 'api_write_password')
    traveler_response = traveler_client.create(form_id, 'dong', 'test create', ['test'])
    assert client.Client.is_json(traveler_response)
    logging.info(traveler_response.json())
