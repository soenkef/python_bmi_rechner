import time
import requests
import json
from urllib.parse import urljoin

class Login():
    def __init__(self):
        payload = {'login': 'mantu@gmx.de', 'password': '57Y.swjtQ*2+LKN'}
        url = "https://api.www.root-me.org/login"
        r = requests.get(url, params=payload)
        cookie = r.headers['Set-Cookie'].split()
        self.spip = cookie[0].strip(";")
        self.spip_list = cookie[0].strip(";").split("=")
        self.spip_value = cookie[0].strip(";").split("=")[1]

    def get_spip(self):
        return self.spip

    def get_challenge(self, value):
        cookies = {"spip_session": self.spip}
        url = "https://api.root-me.org/challenges/ch" + str(value)
        print(url)
        r = requests.get(url, cookies=cookies)
        print(r.headers)


obj = Login()
print(obj.get_spip())
obj.get_challenge(58)
