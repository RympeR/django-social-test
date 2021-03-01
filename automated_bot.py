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

    def generate_creds(self, ind):
        name = str(ind)
        login = ''
        for _ in range(random.randint(10, 15)):
            login += ord(random.randint(97, 122))
        login += ind
        password = ''
        for _ in range(random.randint(8, 15)):
            password += ord(random.randint(97, 122))
        password += ord(random.randint(48, 57))
        password += ord(random.randint(65, 90))
        password += '!'
        return name, login, password

    def signup(self, ind):
        creds = self.generate_creds(ind)
        url = self.api_host + "/api/social/user/signup/"
        payload = {
            'name': creds[0],
            'login': creds[1],
            'password': creds[2]
        }

        response = requests.request("POST", url, data=payload)

    def login(self, creds):
        url = self.api_host + "/api/social/user/login/"

        payload = {'login': creds[0],
                   'password': creds[1]}

        response = requests.request(
            "GET", url, data=payload)

    def get_profile(self, ind):

        url = self.api_host + "/api/social/user/get-profile/1"

        response = requests.request("GET", url)

        print(response.text)

    def create_post(self, user_ind, name, image_name):
        url = self.api_host + "/api/social/post/create/"

        payload = {
            'user_id': user_ind,
            'name': name
        }
        files = [
            (
                'image', ('PHZ_0733.jpg',
                          open(
                              '/D:/develop/pypr/django_ecommerce/tokyo_rest/media/PHZ_0733.jpg', 'rb'),
                          'image/jpeg')
            )
        ]
        headers = {}

        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files)

        print(response.text)

    def like_post(self, user_ind, post_ind, like_value):
        url = self.api_host + "/api/social/like/"

        payload = {'post': post_ind,
                   'user': user_ind,
                   'liked': like_value}

        response = requests.request(
            "POST", url, data=payload)

        print(response.text)
