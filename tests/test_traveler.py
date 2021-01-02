import pytest
import logging
from traveler_client import client


@pytest.fixture(scope='module')
def traveler_fixture():
    from traveler_client import traveler
    return traveler.Traveler('https://localhost:3443', 'api_write', 'api_write_password')


@pytest.fixture(scope='module')
def state_fixture():
    return {'form_id': '5fe6817cfb700100129f0231', 'traveler_id': None}


def test_create(traveler_fixture, state_fixture):
    traveler_response = traveler_fixture.create(
        state_fixture['form_id'], 'dong', 'test create', ['test'])
    assert client.Client.is_json(traveler_response)
    traveler_response_json = traveler_response.json()
    logging.info(traveler_response_json)
    state_fixture['traveler_id'] = traveler_response_json['_id']
    assert state_fixture['_id']
