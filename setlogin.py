# -*- coding:gbk -*-
# ===== 登录状态模块 =====

from os import path
from client import client

while True:
    if path.isfile('logged'):
        f_logged = open('logged')
        list_logged_info = f_logged.read().split()
        f_logged.close()
        client.set_access_token(list_logged_info[1], list_logged_info[2])
        break
    else:
        import account



