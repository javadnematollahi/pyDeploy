import sys
import time
from functools import partial
from PySide6.QtWidgets import *
# from PySide6.QtGui import *
from PySide6.QtCore import Slot,QTime
# from PySide6.QtGui import QFrame
from ui_mainwindow import Ui_MainWindow
from api import Api_send
from counterthread import CounterThread





class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.get_start.clicked.connect(self.remove_button)
        self.ui.btn_search.clicked.connect(self.search)
        # self.counter = CounterThread()
        # self.counter.signal_show.connect(self.show_counter)


    def remove_button(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.ui.get_start.setFlat(True)
        self.ui.get_start.setText("")
        self.ui.get_start.setStyleSheet(u"background-color: rgb(192, 97, 203);")
        self.ui.get_start.setEnabled(False)

    # def show_counter(self, count):
    #     self.ui.counterr.setText(str(count))

    def search(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        city = self.ui.lineEdit.text()
        if city != "":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6)
            self.api = Api_send(city)
            self.api.signal_show.connect(self.show_temp)
            self.api.start()
            # self.counter.start()
            
            c = 0
            # while True:
            #     if int(self.ui.counterr.placeholderText())>10:
            #         self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3)
            #         break
            for _ in range(15):
                c += 1
                time.sleep(1)
                print(c)
                if c > 10:
                    self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3)
                    break

            # print(response.text)
        else:
            print("CC")
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5)
            print("DD")

    def show_temp(self,res):
        try:
            self.ui.textBrowser_2.setText(res['temperature'])
            self.ui.textBrowser_6.setText(res['description'])
            self.ui.textBrowser_4.setText(res['wind'])
            self.ui.textEdit_3.setText(res['forecast'][0]['temperature'])
            self.ui.textEdit_4.setText(res['forecast'][0]['wind'])
            self.ui.textEdit_6.setText(res['forecast'][1]['temperature'])
            self.ui.textEdit_5.setText(res['forecast'][1]['wind'])
            self.ui.textEdit_10.setText(res['forecast'][2]['temperature'])
            self.ui.textEdit_8.setText(res['forecast'][2]['wind'])
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)
        except:
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Mainwindow()
    window.show()

    app.exec()
    