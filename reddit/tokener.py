import requests
import os
import json


class Tokener:
    def __init__(self):
        self.username = os.environ.get('REDDIT_USERNAME')
        self.password = os.environ.get('REDDIT_PASSWORD')
        self.appid = os.environ.get('TEST_MY_REST_RD_APP_ID')
        self.appsecret = os.environ.get('TEST_MY_REST_RD_APP_SECRET')

        self.base_url = 'https://www.reddit.com'

        self.data = {'grant_type': 'password', 'username': self.username, 'password': self.password}

        self.auth = requests.auth.HTTPBasicAuth(self.appid, self.appsecret)

        self.r = requests.post(
            self.base_url + 'api/v1/access_token',
            data = self.data,
            headers = {'user-agent': 'test-my-rest by thirstyfountain'},
            auth = self.auth
        )

        self.token = self.r.json()['access_token']

    def getToken(self):
        return self.token
