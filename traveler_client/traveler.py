import datetime
from .client import Client


class Traveler:
    def __init__(self, base, user, pw):
        self.client = Client(base, user, pw)

    def __gen_title(self, title):
        if title:
            return title
        return datetime.datetime.now()

    def create(self, form_id, user_id, title=None, devices=None):
        return self.client.request('post', '/apis/create/traveler/', json={'formId': form_id, 'userName': user_id, 'title': self.__gen_title(title), 'devices': devices })

    def update_status(self, traveler_id, status, user_id):
        return self.client.request('put', f'/apis/travelers/{traveler_id}/status/', json={'status': status, 'userName': user_id})