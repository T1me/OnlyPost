# -*- coding:GBK -*-
# ===== ����tokenģ�� =====

from client import client

auth_url = client.get_authorize_url()
# TODO: redirect to url

print "\n[��Ȩҳ��]" + auth_url

requ_code = raw_input("\n[������Ȩ����ת��URL�е�������]")

print

r = client.request_access_token(requ_code)

access_token = r.access_token

expires_in = r.expires_in

uid = r.uid
