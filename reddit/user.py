import requests
import time
from reddit.tokener import Tokener

reddit = 'https://oauth.reddit.com/'

token = 'bearer ' + Tokener().getToken()

headers = {'Authorization': token, 'User-Agent': 'test-my-rest by thirstyfountain'}


class User:
    def __init__(self, u):
        self.name = u

    def getAbout(self):
        return requests.get(reddit + '/user/' + self.name + '/about', headers=headers)

    def getKarma(self):
        return requests.get(reddit + '/api/v1/me/karma', headers=headers)

    def getComments(self):
        return requests.get(reddit + '/api/v1/me', headers=headers)

    def getTrophies(self):
        return requests.get(reddit + '/api/v1/user/' + self.name + '/trophies', headers=headers)

    def getCreationDate(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.getAbout().json()['data']['created']))