import requests
import json

class Common():

    def __init__(self):
        self.cookie_string = ''

        with open("cookie", "r") as f:  # 打开文件
            self.cookie_string = f.read()  # 读取文件

    def GetSigned(self, uid):

        header = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Connection": "keep-alive",
            "Referer": "https://link.bilibili.com/p/center/index",
            "TE": "Trailers",
            'Cookie': self.cookie_string

        }

        r = requests.get('https://api.live.bilibili.com/live_user/v1/GuildMaster/searchAnchor?uid=' + uid,
                         headers=header)  # 最基本的不带参数的get请求
        if r.status_code == 200:
            if r.text != "":
                js = json.loads(r.text)
                data = js['data']
                if data != None and len(data) > 0:
                    room_id = data['items'][0]['roomid']
                    uname = data['items'][0]['uname']
                    is_signed = data['items'][0]['is_signed']
                    return room_id, uname, is_signed
        else:
            return ""