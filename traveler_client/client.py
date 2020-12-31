# import configparser
import requests
import logging


class Client:
    def __init__(self, base, user, pw):
        # config = configparser.ConfigParser()
        # print(ini)
        # config.read(ini)
        # print(config.sections())
        self.base = base
        # the agent header
        self.headers = {'user-agent': 'python-traveler-client/0.0.1'}
        # 4 seconds
        self.timeout = 4
        # auth
        self.auth = (user, pw)
        # do not verify cert
        self.verify=False

    def request(self, method, path, json=None):
        url = self.base + path
        logging.debug(url)
        return requests.request(method=method, url=url, auth=self.auth, json=json, headers=self.headers, timeout=self.timeout, verify=self.verify)

    @staticmethod
    def is_json(response):
        if response.headers['content-type'].find('json'):
            return True
        return False

    @staticmethod
    def json(response):
        if response.headers['content-type'].find('json'):
            return response.json()
        return None
