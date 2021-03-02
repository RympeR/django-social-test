import random
from decouple import config
import requests
from random import randint, choice
from progress.bar import IncrementalBar

config.encoding = 'utf-8'



NUMBER_OF_USERS = config('NUMBER_OF_USERS')
MAX_POSTS_PER_USER = config('MAX_POSTS_PER_USER')
MAX_LIKES_PER_USER = config('MAX_LIKES_PER_USER')
API_HOST = config('API_HOST')


class UserBot:

    def __init__(self, number_of_users, max_posts_per_user, max_like_per_user, api_host):
        self.number_of_users = int(number_of_users)
        self.max_posts_per_user = int(max_posts_per_user)
        self.max_like_per_user = int(max_like_per_user)
        self.api_host = api_host

    def generate_creds(self, ind):
        name = str(ind)
        login = ''
        for _ in range(random.randint(10, 15)):
            login += chr(random.randint(97, 122))
        login += str(ind)
        password = ''
        for _ in range(random.randint(8, 15)):
            password += chr(random.randint(97, 122))
        password += chr(random.randint(48, 57))
        password += chr(random.randint(65, 90))
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

        response = requests.post(url, json=payload)

        return response.text

    def login(self, creds):
        url = self.api_host + "/api/social/user/login/"

        payload = {
            "login": creds[0],
            "password": creds[1]
        }
        response = requests.request(
            "GET", url, json=payload)

        return response.json()

    def get_profile(self, ind):

        url = self.api_host + "/api/social/user/get-profile/"+str(ind)
        response = requests.request("GET", url)
        return response.json()

    def create_post(self, user_ind, name, image_name=''):
        url = self.api_host + "/api/social/post/create/"

        payload = {
            'user_id': user_ind,
            'name': name
        }
        
        files = [
            ('image', ('PHZ_0733.jpg', open(
                'D:/develop/pypr/django_ecommerce/tokyo_rest/media/PHZ_0733.jpg', 'rb'), 'image/jpeg'))
        ]

        response = requests.post(url, json=payload, files=files)

        return response

    def like_post(self, user_ind, post_ind, like_value):
        url = self.api_host + "/api/social/like/"

        payload = {'post': post_ind,
                   'user': user_ind,
                   'liked': like_value}
        response = requests.request(
            "POST", url, json=payload)

        print(response.text)

    def bot_loop(self):
        users = []
        posts = []
        # user_bar = IncrementalBar('Users', max = self.number_of_users)
        # posts_bar = IncrementalBar('Posts', max = self.max_posts_per_user)
        # likes_bar = IncrementalBar('Likes', max = self.max_like_per_user)git sta
        for _ in range(self.number_of_users):
            # user_bar.next()
            data = self.signup(_)
            users.append(['user'])
            for i in range(self.max_posts_per_user):
                # posts_bar.next()
                posts.append(self.create_post(_, i)['post'])

        for user_id in users:
            for like in self.max_like_per_user:
                post = choice(posts)
                # likes_bar.next()
                self.like_post(
                    user_id,
                    post,
                    True if randint(1, 3) == 2 else False
                )


def main():
    userbot = UserBot(
        NUMBER_OF_USERS,
        MAX_POSTS_PER_USER,
        MAX_LIKES_PER_USER,
        API_HOST
    )
    userbot.signup(
        5
    )


if __name__ == "__main__":
    main()
