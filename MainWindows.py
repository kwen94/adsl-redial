import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from GuiThread import BigWorkThread
from ui_mainwindow import Ui_Dialog
from map import route

import threading

class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.events = threading.Event()

        self.pushButton.clicked.connect(lambda: self.BigWork('urgent'))
        # self.pushButton_2.clicked.connect(lambda: self.BigWork('common'))

    def BigWork(self, action):
        widget_dict = route(self, action)
        self.Button = widget_dict.get('Button')
        self.PlainTextEdit = widget_dict.get('PlainTextEdit')
        self.SpinBox = widget_dict.get('SpinBox')
        self.Label_ip = widget_dict.get('Label_ip')
        self.Label_c_time = widget_dict.get('Label_c_time')
        self.LineEdit_name = widget_dict.get('LineEdit_name')
        self.LineEdit_username = widget_dict.get('LineEdit_username')
        self.LineEdit_password = widget_dict.get('LineEdit_password')


        # print(self.Button, self.PlainTextEdit,self.SpinBox)

        self.Button.setFocus()
        text = self.Button.text()

        if text == 'run...':
            self.events.set()
        else:
            self.Button.setText('run...')
            # 新建对象，给子进程传入参数
            self.bwThread = BigWorkThread(self.events, self,  text, action)
            # 连接子进程的信号和槽函数
            self.bwThread.finishSignal.connect(self.BigWorkEnd)
            # 开始执行 run() 函数里的内容
            self.bwThread.start()

    def BigWorkEnd(self, subThreadResultdic:dict):
        # print('end')
        if subThreadResultdic.get('name') == 'main':
            self.Button.setText(subThreadResultdic.get('text'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

