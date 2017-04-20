# -*- coding:gbk -*-

from weibo import APIClient

APP_KEY = '93591061'
APP_SECRET = '2cfe37489ae15946201449baee2c8b94'
CALLBACK_URL = 'http://118.89.50.34'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

auth_url = client.get_authorize_url()
# TODO: redirect to url

print "\n[授权页面]" + auth_url

requ_code = raw_input("\n[输入授权后跳转的URL中的请求码]")

print

r = client.request_access_token(requ_code)

access_token = r.access_token

expires_in = r.expires_in

client.set_access_token(access_token, expires_in)

client.statuses.update.post(status=u'test')
