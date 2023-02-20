import pytest
import logging
from traveler_client import client, traveler


@pytest.fixture(scope='module')
def traveler_fixture():
    from traveler_client import traveler
    return traveler.Traveler('http://localhost:3002', 'api_write', 'api_write_password')


@pytest.fixture(scope='module')
def state_fixture():
    return {'form_id': '5ff0abd8de8f2600ef9eda2d', 'traveler_id': None, 'traveler_status': None,'traveler_mapping': None, 'traveler_types': None}


def test_create(traveler_fixture, state_fixture):
    traveler_response = traveler_fixture.create(
        state_fixture['form_id'], 'dong', 'test create', ['test'])
    assert client.Client.is_json(traveler_response)
    traveler_response_json = traveler_response.json()
    logging.info(traveler_response_json)
    state_fixture['traveler_id'] = traveler_response_json['_id']
    assert state_fixture['traveler_id']
    state_fixture['traveler_status'] = traveler_response_json['status']
    assert state_fixture['traveler_status'] == 0
    state_fixture['traveler_mapping'] = traveler_response_json['mapping']
    assert state_fixture['traveler_mapping']
    state_fixture['traveler_types'] = traveler_response_json['types']
    assert state_fixture['traveler_types']

def test_update_status(traveler_fixture, state_fixture):
    status = 1
    traveler_response = traveler_fixture.update_status(state_fixture['traveler_id'], status, 'dong')
    assert traveler_response.ok
    if traveler_response.status_code == 200:
       assert client.Client.is_json(traveler_response)
       traveler_response_json = traveler_response.json()
       assert traveler_response_json['status'] == status

def test_insert_date(traveler_fixture, state_fixture):
    name = state_fixture['traveler_mapping']['text']
    value = 'python test'
    input_type = state_fixture['traveler_types'][name]
    data_response = traveler_fixture.insert_data(state_fixture['traveler_id'], name, value, input_type, 'dong')
    assert data_response.ok
    name = state_fixture['traveler_mapping']['number']
    value = 5
    input_type = state_fixture['traveler_types'][name]
    data_response = traveler_fixture.insert_data(state_fixture['traveler_id'], name, value, input_type, 'dong')
    assert data_response.ok
    name = state_fixture['traveler_mapping']['boolean']
    value = True
    input_type = state_fixture['traveler_types'][name]
    data_response = traveler_fixture.insert_data(state_fixture['traveler_id'], name, value, input_type, 'dong')
    assert data_response.ok