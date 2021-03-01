import random
from decouple import config
import requests
from random import randint, choice

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
        headers = {
            'content-type':'multipart/form-data; '
        }
        response = requests.request("POST", url,headers=headers, data=payload)
        return response.text

    def login(self, creds):
        url = self.api_host + "/api/social/user/login/"

        payload = {'login': creds[0],
                   'password': creds[1]}
        headers = {
            'content-type':'multipart/form-data; '
        }
        response = requests.request(
            "GET", url,headers=headers, data=payload)

    def get_profile(self, ind):

        url = self.api_host + "/api/social/user/get-profile/1"
        headers = {
            'content-type':'multipart/form-data; '
        }
        response = requests.request("GET", url,headers=headers)

        print(response.text)

    def create_post(self, user_ind, name, image_name=''):
        url = self.api_host + "/api/social/post/create/"

        payload = {
            'user_id': user_ind,
            'name': name
        }
        files = [
            (
                'image', ('PHZ_0733.jpg',
                          open('PHZ_0733.jpg', 'rb'),
                          'image/jpeg')
            )
        ]
        headers = {
            'content-type':'multipart/form-data; '
        }

        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files)

        return response

    def like_post(self, user_ind, post_ind, like_value):
        url = self.api_host + "/api/social/like/"

        payload = {'post': post_ind,
                   'user': user_ind,
                   'liked': like_value}
        headers = {
            'content-type':'multipart/form-data; '
        }
        response = requests.request(
            "POST", url,headers=headers, data=payload)

        print(response.text)

    def bot_loop(self):
        users = []
        posts = []
        for _ in range(self.number_of_users):
            data = self.signup(_)
            print(data)
            users.append(['user'])
            for i in range(self.max_posts_per_user):
                posts.append(self.create_post(_, i)['post'])
            
        for user_id in users:
            for like in self.max_like_per_user:
                post = choice(posts)
                self.like_post(
                    user_id,
                    post,
                    True if randint(1, 3)==2 else False
                )
def main():
    userbot = UserBot(NUMBER_OF_USERS, MAX_POSTS_PER_USER, MAX_LIKES_PER_USER, API_HOST)
    userbot.bot_loop()

if __name__ == "__main__":
    main()
