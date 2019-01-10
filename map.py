import time
import requests


def route(self, action):
    widget_name_dic = {}
    if action == 'urgent':
        widget_name_dic['Button'] = self.pushButton
        widget_name_dic['PlainTextEdit'] = self.plainTextEdit
        widget_name_dic['SpinBox'] = self.spinBox
        widget_name_dic['Label_ip'] = self.label_3
        widget_name_dic['Label_c_time'] = self.label_6
        widget_name_dic['LineEdit_name'] = self.lineEdit
        widget_name_dic['LineEdit_username'] = self.lineEdit_2
        widget_name_dic['LineEdit_password'] = self.lineEdit_3
    if action == 'common':
        widget_name_dic['Button'] = self.pushButton_2

    return widget_name_dic


def format_time(lst):
    new_lst = []
    for i in lst:
        go_time = time.strftime("%Y-%m-%d")
        go_datetime = '{} {}:00'.format(go_time, i)
        # print(go_datetime)
        timeStruct = time.strptime(go_datetime, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeStruct))
        new_lst.append(timeStamp)
    return new_lst


def get_ip(ip=None):
    ip_info = '网络请求失败'
    try:
        info = requests.get('https://www.ip.cn/{}'.format(ip),headers={"User-Agent":"curl/7.29.0"}).text.split()
        tmp = [info[2], info[4], info[5]]
        ip_info = ' '.join(tmp)
    except:
        pass

    return ip_info
