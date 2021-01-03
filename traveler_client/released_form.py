from .client import Client


class ReleasedForm:
    def __init__(self, base, user, pw):
        self.client = Client(base, user, pw)

    def get_all(self):
        return self.client.request('get', '/apis/releasedForms/')

    def get(self, formId):
        return self.client.request('get', f'/apis/releasedForms/{formId}/')
