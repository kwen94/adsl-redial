from PyQt5 import QtCore
import time

from map import format_time, get_ip
from change import Network


class BigWorkThread(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(dict)

    def __init__(self, events, main_self, text, action):
        super(BigWorkThread, self).__init__()
        self.events = events
        self.text = text
        self.main_self = main_self
        self.action = action
        self.cron = None
        self.network = Network(main_self.LineEdit_name.text(), main_self.LineEdit_username.text(), main_self.LineEdit_password.text())

        if self.main_self.PlainTextEdit is not None:
            tmp = self.main_self.PlainTextEdit.toPlainText()
            self.cron = list(map(lambda x: x.strip(' '), ''.join(tmp).split('\n')))
            self.cron = format_time(self.cron)

        if self.main_self.SpinBox is not None:
            self.interval = int(self.main_self.SpinBox.text())

    def is_change(self, now, strTime, t):
        # print(now + self.interval * 60, t)
        if now + self.interval * 60 == t:
            # print('True')
            self.network.disconnect()
            code = self.network.connect()
            if code == 0:
                ip_info = get_ip()
                # print(ip_info)
                self.main_self.Label_ip.setText(ip_info)
                self.main_self.Label_c_time.setText(strTime)

    def urgent_work(self):
        result = {'name': 'main', 'text': self.text}

        while not self.events.wait(1):
            if self.cron is not None:
                now = int(time.time())
                localTime = time.localtime(now)
                strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
                for t in self.cron:
                    self.is_change(now, strTime, t)

        self.events.clear()
        return result




    def common_work(self):
        pass

    def run(self):

        if self.action == 'urgent':
            res = self.urgent_work()
        elif self.action == 'common':
            res = self.common_work()
        self.finishSignal.emit(res)
