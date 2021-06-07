import time
from urllib import request
import json

from configparser import ConfigParser

TOKEN_FILE = 'token.cfg'


class Session:

    def __init__(self):
        self.protocol = 'https://'
        self.address = 'api.vk.com/method/'
        self.token_field = f'access_token={self.get_token()}'

    def get_friends(self, user_id=''):
        method = 'friends.get'
        if user_id != '':
            user_id = f'user_id={user_id}&'
        response = request.urlopen(f'{self.protocol}{self.address}{method}?{user_id}v=5.52&{self.token_field}')
        json_response = json.load(response)
        if 'error' in json_response:
            return json_response['error']['error_msg']
        print(f'Wait please. We have to handle {json_response["response"]["count"]} persons')
        return self.parse_ids(json_response['response']['items'])

    @staticmethod
    def get_token():
        parser = ConfigParser()
        with open(TOKEN_FILE) as t_file:
            parser.read_file(t_file)
        return parser["Token"]["Token"]

    def parse_id(self, user_id):
        method = 'users.get'
        user_id = f'user_id={user_id}&'
        response = request.urlopen(f'{self.protocol}{self.address}{method}?{user_id}v=5.52&{self.token_field}')
        json_response = json.load(response)
        return json_response['response']

    def parse_ids(self, ids):
        users = []
        for user_id in ids:
            time.sleep(0.33)
            user = self.parse_id(user_id)[0]
            users.append(f'{user["first_name"]} {user["last_name"]}: {user["id"]}')
        return '\n'.join(users)
