import requests
from requests.auth import HTTPBasicAuth
from utility.configurations import *


class RestApi:
    def __init__(self):
        self.username = getConfig()['con_config']['username']
        self.baseURL = getConfig()['API']['endpoint']
        self.auth = HTTPBasicAuth(self.username, getConfig()['con_config']['passkey'])
        print(self.username)

    def GET_Method(self, url,auth):
        self.response = requests.get(url, auth=auth)
        return self.response.status_code, self.response.json()


    def POST_Method(self, url, json_payload, auth, headers):

        self.response = requests.post(url, json=json_payload, auth=auth, headers = headers)
        return self.response.status_code, self.response.json()

    
    def PATCH_Method(self, url, json_payload, auth, headers):
        self.response = requests.patch(url, json=json_payload, auth=auth, headers = headers)
        return self.response.status_code, self.response.json()


    def DELETE_METHOD(self, url, auth):
        self.response = requests.delete(url, auth=auth)
        return self.response.status_code








