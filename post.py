# -*- coding:gbk -*-
# 

from setlogin import client

text_post = raw_input(u"\n[Only Post]~> ")

try:
    client.statuses.update.post(status=text_post)
    print "[���ͳɹ�]\n"
except:
    print "[����ʧ��]\n"
print
