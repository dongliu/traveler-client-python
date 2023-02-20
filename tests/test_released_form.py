import logging
from traveler_client import released_form, client


def test_get_all():
    form_client = released_form.ReleasedForm('http://localhost:3002', 'api_write', 'api_write_password')
    form_response = form_client.get_all()
    assert client.Client.is_json(form_response)
    # logging.info(form_response.json())

def test_get():
    form_client = released_form.ReleasedForm('http://localhost:3002', 'api_write', 'api_write_password')
    all_form_response = form_client.get_all()
    assert client.Client.is_json(all_form_response)
    all_form = all_form_response.json()
    assert len(all_form) > 0
    form_id = all_form[0]['_id']
    form_response = form_client.get(form_id)
    assert client.Client.is_json(form_response)
    logging.info(form_response.json())