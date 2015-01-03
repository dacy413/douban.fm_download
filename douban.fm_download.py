#########################################
# download song of douban.fm
#########################################
import requests

class DouBanFM(object):
    """docstring for DouBan"""
    def __init__(self):
        self.user_name = ""
        self.password = ""

    def getUserINfo(self):
        self.user_name = "1656505353@qq.com"
        self.password = "05152842413"

    def login(self):
        login_data = {
        'app_name':'radio_desktop_win',
        'version':100,
        'email':self.user_name,
        'password':self.password
        }
        import pdb;pdb.set_trace()
        
        t_res = requests.post('http://www.douban.com/j/app/login', login_data)
        

        like_data = {
        'app_name':'radio_desktop_win',
        'version':100,
        'email':self.user_name,
        'password':self.password
        }
        http://douban.fm/j/play_record?ck=gnzw&spbid=%3A%3A&type=liked
        print("result of login ====>>",t_res.text)


if __name__ == '__main__':
    dbf = DouBanFM()
    dbf.getUserINfo()
    dbf.login()