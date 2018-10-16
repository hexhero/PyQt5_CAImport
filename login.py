import requests

url = "http://101.37.28.80/kingbao-web-admin/auth/login"

def login(username,password):
    r = requests.post(url,data={"username":username,"password":password})
    if r.status_code == 200:
        return "apl_cookies" + "=" + r.request._cookies.get("apl_cookies")
        
if __name__ == "__main__":
    print(login("jb18","888888"))