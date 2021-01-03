# traveler-client-python

This repo is a simple traveler client programed in python. The client can
perform the following interactions:

- retrieve all forms
- retrieve all released forms
- retrieve a released form with a given id
- create a new traveler instance for devices from a released form
- update the status of a traveler
- save data into a given traveler instance

The tests shows how to perform these interactions. The `tests/test_traveler.py`
test shows the flow of create a new traveler and update it from a released form,
which can be added into a local environment from the file
`tests/5ff0abd8de8f2600ef9eda2d.json`. The form contains three inputs of basic
types: text, number, and boolean. It shows how to insert data into a traveler
using the `keys` defined by the user when creating the form.

## project configuration

The `Pipfile` has all the dependencies for runtime and development. A virtual
environment can be managed with `pipenv`. The python version can be managed with
`pyenv`.