import time
import requests
import json
from urllib.parse import urljoin

class Login():
    def __init__(self):
        payload = {'login': 'mantu@gmx.de', 'password': '57Y.swjtQ*2+LKN'}
        url = "https://api.www.root-me.org/login"
        with requests.get(url, params=payload) as r:
            cookie = r.headers['Set-Cookie'].split()
            self.spip = cookie[0].strip(";")
            self.spip_list = cookie[0].strip(";").split("=")
            self.spip_value = cookie[0].strip(";").split("=")[1]

    def get_spip(self):
        return self.spip_value

    def get_challenge(self, value):
        spip = {"spip_session": str(self.get_spip())}
        #url = "https://api.www.root-me.org/challenges/" + str(value)
        url = "https://api.www.root-me.org/auteurs/" + str(value)
        #print(url)
        with requests.get(url, cookies=spip) as r:
            print(r.content)


obj = Login()
#print(obj.get_spip())
obj.get_challenge(60)
