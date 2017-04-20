# -*- coding:gbk -*-
# 

from setlogin import client

text_post = raw_input(u"\n[Only Post]~> ")

try:
    client.statuses.update.post(status=text_post)
    print "[发送成功]\n"
except:
    print "[发送失败]\n"
print
