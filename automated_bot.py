import random
from decouple import config
import requests

config.encoding = 'utf-8'

NUMBER_OF_USERS = config('NUMBER_OF_USERS')
MAX_POSTS_PER_USER = config('MAX_POSTS_PER_USER')
MAX_LIKES_PER_USER = config('MAX_LIKES_PER_USER')
API_HOST = config('API_HOST')


class UserBot:

    def __init__(self, number_of_users, max_posts_per_user, max_like_per_user, api_host):
        self.number_of_users = number_of_users
        self.max_posts_per_user = max_posts_per_user
        self.max_like_per_user = max_like_per_user
        self.api_host = api_host

    def generate_creds(self):
        login = ''
        for _ in range(random.randint(10, 15)):
            login += ord(random.randint(97, 122))
        password = ''
        for _ in range(random.randint(8, 15)):
            password += ord(random.randint(97, 122))
        password += ord(random.randint(48, 57))
        password += ord(random.randint(65, 90))
        password += '!'
        return login, password

    def signup(self):
        creds = self.generate_creds()
    
    def create_psot(self):
        ...
    
    def like_post(self):
        ...