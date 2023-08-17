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


    # def get_NDG(self):
    #     data_json = {
    #         "NetworkDeviceGroup": {
    #             "name": "ringnet",
    #             "description": "Group description",
    #             "ndgtype": "Device Type#All Device Types#"
    #         }
    #         }
        # conn = requests.get(url="https://{}:9060/ers/config/networkdevicegroup/name/Device Type:All Device Types:ringnet4".format(self.ISE_IP),  #특정 디바이스그룹의 속성 확인 조회
        conn = requests.get(url="https://{}:9060/ers/config/networkdevicegroup".format(self.ISE_IP),    #디바이스 그룹이 어떤게 있는 지 조회
                headers = self.HEADER_JSON,
                auth = self.AUTH_INFO,
                # data=json.dumps(data_json),
                verify = False)
        print(conn.content)


ISE_TEST = isebsh('192.168.82.21','admin','Ringnet01!')
# ISE_TEST.get_NDG()

#AAAA22