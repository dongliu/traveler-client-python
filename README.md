# traveler-client-python

This repo is a simple traveler client programed in python. The client can
perform the following interactions:

- retrieve all forms
- retrieve all released forms
- retrieve a released form with a given id
- create a new traveler instance for devices from a released form
- update the status of a traveler
- save data into a given traveler instance

The tests shows how to perform these interactions. 

The `tests/test_traveler.py` test shows the flow of create a new traveler and
update it from a released form. In order to seed the released form, create a new
document in the local collection `releasedforms` with the content of
`tests/5ff0abd8de8f2600ef9eda2d.bson`. The form contains three inputs of basic
types: text, number, and boolean. It shows how to insert data into a traveler
using the `keys` defined by the user when creating the form.

The tests were passed with https://github.com/dongliu/traveler/pull/137

## project configuration

The `Pipfile` has all the dependencies for runtime and development. For Mac,
```
brew install python3
python3 -m ensurepi
pip3 install pipenv
pipenv install --dev
pipenv shell
pytest tests/test_form.py
```