import pytest
import logging
from traveler_client import client, traveler


@pytest.fixture(scope='module')
def traveler_fixture():
    from traveler_client import traveler
    return traveler.Traveler('https://localhost:3443', 'api_write', 'api_write_password')


@pytest.fixture(scope='module')
def state_fixture():
    return {'form_id': '5ff0abd8de8f2600ef9eda2d', 'traveler_id': None, 'traveler_mapping': None, 'traveler_types': None}


def test_create(traveler_fixture, state_fixture):
    traveler_response = traveler_fixture.create(
        state_fixture['form_id'], 'dong', 'test create', ['test'])
    assert client.Client.is_json(traveler_response)
    traveler_response_json = traveler_response.json()
    logging.info(traveler_response_json)
    state_fixture['traveler_id'] = traveler_response_json['_id']
    assert state_fixture['traveler_id']
    state_fixture['traveler_mapping'] = traveler_response_json['mapping']
    assert state_fixture['traveler_mapping']
    state_fixture['traveler_types'] = traveler_response_json['types']
    assert state_fixture['traveler_types']
