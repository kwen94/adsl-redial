import datetime
import subprocess

class Network:
    def __init__(self, name=None, username=None, password=None):
        self.name = name
        self.username = username
        self.password = password

    def connect(self):
        command = 'rasdial {} {} {}'.format(self.name, self.username, self.password)
        return self.exec(command, '连接')

    def disconnect(self):
        command = 'rasdial {} /disconnect'.format(self.name)
        return self.exec(command, '断开连接')

    def exec(self, command, action):
        try:
            code = subprocess.getstatusoutput(command)[0]
        except:
            code = 1

        if code == 0:
            print('{}成功'.format(action))
        else:
            print('{}失败'.format(action))
        return code

    def log(self, info):
        date = datetime.datetime.now()
        with open('c:/adsl.log', 'a') as f:
            f.write(str(date) + info)


        # adsl = Network('宽带连接', 'yladsl', '123456')




