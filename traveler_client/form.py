from .client import Client


class Form:
    def __init__(self, base, user, pw):
        self.client = Client(base, user, pw)

    def get_all(self):
        return self.client.request('get', '/apis/forms/')
