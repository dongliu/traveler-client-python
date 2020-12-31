import logging
from traveler_client import form, client


def test_get_all():
    form_client = form.Form('https://localhost:3443', 'api_write', 'api_write_password')
    form_response = form_client.get_all()
    assert client.Client.is_json(form_response)
    logging.info(form_response.json())

