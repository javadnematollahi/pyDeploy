import time
from PySide6.QtCore import QThread,Signal
import requests
import json


class Api_send(QThread):

    signal_show=Signal(dict)

    def __init__(self,city):
        super().__init__()
        self.city = city

    def run(self):
        url = f"https://goweather.herokuapp.com/weather/{self.city}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        self.signal_show.emit(json.loads(response.text))

