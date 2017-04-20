# -*- coding:GBK -*-
# ===== 请求token模块 =====

from client import client

auth_url = client.get_authorize_url()
# TODO: redirect to url

print "\n[授权页面]" + auth_url

requ_code = raw_input("\n[输入授权后跳转的URL中的请求码]")

print

r = client.request_access_token(requ_code)

access_token = r.access_token

expires_in = r.expires_in

uid = r.uid
