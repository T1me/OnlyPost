# -*- coding:gbk -*-
# ===== 帐号管理模块 =====

from os import path
from client import client

if path.isfile('token') == False:
    f_token = open('token', 'w')
    f_token.close()
# 检测token记录否则创建新文件

dict_uid = {}
f_token = open('token')
list_lines = f_token.readlines()
f_token.close()
for line in list_lines:
    list_UTE = line.split()
    dict_uid[list_UTE[0]] = [list_UTE[1] , list_UTE[2]]
# 构建uid字典

empty = True
print "\n[已授权uid]"
for k in dict_uid.iterkeys():
    print k
    empty = False
if empty:
    print "(empty)"
print "=========="
logining_uid = ""
while len(logining_uid) != 10:
    logining_uid = raw_input("[请输入需要登录的微博uid]")
print
# 输入登录的uid

logged_w = ""

if dict_uid.has_key(logining_uid):
    access_token = dict_uid[logining_uid][0]
    expires_in = dict_uid[logining_uid][1]
    logged_w = logining_uid + " " + dict_uid[logining_uid][0] + " " + dict_uid[logining_uid][1]
else:
    from req_token import client, uid, access_token, expires_in
    f_token = open('token', 'a')
    token_w = uid + " " + access_token + " " + str(expires_in) + "\n"
    f_token.write(token_w)
    f_token.close()
    print "\nToken已保存\n"
    logged_w = token_w
# 判断用户是否已授权，未授权则要求授权

f_logged = open('logged', 'w')
f_logged.write(logged_w)
f_logged.close()
print "[登录成功]\n"
# 将帐号信息保存至logged等待登录状态模块读取
