import requests
import urllib3,json

class isebsh():
    def __init__(self,IP,USER,PASS):
        urllib3.disable_warnings()
        self.ISE_IP = IP
        self.ISE_USER = USER
        self.ISE_PASS = PASS
        self.HEADER_JSON = {'accept': 'application/json',
                            'Content-Type': 'application/json',
                            'Authorization': 'Basic YWRtaW46UmluZ25ldDAxIQ==',
                            'Cache-Control': 'no-cache'}
        self.AUTH_INFO = (self.ISE_USER,self.ISE_PASS)


    def update_user(self):
        data_json = {
           "InternalUser" : {
           "enabled" : "false",
           "passwordIDStore": "ad1",
            }
       }
        conn = requests.put(url="https://{}:9060/ers/config/internaluser/name/testuser03".format(self.ISE_IP),
                headers = self.HEADER_JSON,
                auth = self.AUTH_INFO,
                data=json.dumps(data_json),
                verify = False)
        print(conn.content)


ISE_TEST = isebsh('192.168.82.21','admin','Ringnet01!')
ISE_TEST.update_user()