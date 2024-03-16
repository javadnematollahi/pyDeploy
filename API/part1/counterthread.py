import time
from PySide6.QtCore import QThread,Signal
import requests
import json


class CounterThread(QThread):

    signal_show=Signal(int)

    def __init__(self):
        super().__init__()
        self.count = 0


    def run(self):
        while True:
            self.count +=1
            time.sleep(1)
            self.signal_show.emit(self.count)
            if self.count >15:
                break
        
