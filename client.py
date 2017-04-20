# -*- coding:gbk -*-
# ===== 客户端信息生成模块 =====

from weibo import APIClient

APP_KEY = '93591061'
APP_SECRET = '2cfe37489ae15946201449baee2c8b94'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
