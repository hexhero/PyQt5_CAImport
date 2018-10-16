import csv
import json
import time

import requests

from login import login

print(
    '''
    数据导入程序
                                -----杨斌 2018-10-15
    '''
)

class yangb(object):

    username = None

    did = {"jb1":81,"jb2":101,"jb3":102,"jb4":103,"jb5":104,"jb6":105,"jb7":106,"jb8":107,"jb9":108,"jb10":109,"jb11":110,"jb12":111,"jb13":112,"jb14":113,"jb15":114,"jb16":115,"jb17":116,"jb18":117,"jb19":118,"xlp":119,"why":120,"liangt":121,"wqq":122,"jb24":123}

    param = {
        "id":"16",
        "appCodeName": "金华人力资源和社会保障局",
        "appCode": "sb_330700",
        "certPolicyName": "金华社保RSA企业证书策略 机构证书-RSA-自签根",
        "certPolicy": "jhsb-ent-rsa",
        "createUserId": "101",
        "createDate": "1513054203000",
        "updateUserId": "101",
        "updateDate": "1521623235000",
        "stauts": 1,
        "feeScale": "20170207_jhsb_ent_new",
        "feeScaleSelected[id]": "180",
        "feeScaleSelected[name]": "金华社保首张证书新领免费，第二张证书开始收费200元/张",
        "feeScaleSelected[value]": "20170207_jhsb_ent_new",
        "feeScaleSelected[scope]": "CA收费策略",
        "feeScaleSelected[type]": 38,
        "feeScaleSelected[available]": 1,
        "feeScaleSelected[createUserId]": 101,
        "feeScaleSelected[createDate]": 1519814629000,
        "feeScaleSelected[updateUserId]": 101,
        "feeScaleSelected[updateDate]": 1519814629000,
        "feeScaleSelected[orgCode]": "ZJAPL",
        "name": "金华市正升工艺品有限公司",
        "hrssCode": "07093997",
        "zipCode": "321000",
        "address": "浙江省金华市金东区孝顺镇镇北功能区十八号地块1幢3楼",
        "linkMan": "金华社保",
        "linkMobile": "18267918173",
        "linkIdCode": "330703198104029597",
        "unitedCode": "91330703MA28EDD53A",
        "certApp": "sb_330700",
        "province": "浙江省",
        "city": "金华市",
        "area": "婺城区",
        "districtId": 118, # jb18 117 | jb2 101 |jb17 116 |jb19 118
        "certAmount": 1,
        "fileIds": "",
        "count": 1,
        "businessType": 1

        }
    
    def __init__(self):
        pass

    def trans(self,username, filepath,func=None):
        head={"cookie":"apl_cookies=6dc53a05-cbaf-4580-9fb5-e58f9840c1fd","Content-Type":"application/x-www-form-urlencoded;charset=utf-8"}

        head["cookie"] = login(username,"888888")

        yangb.param['districtId'] = yangb.did[username]

        with open(filepath,'r',encoding='utf-8') as f:
            print("开始导入>>>>>>>>>>>>>>>>>>")
            reader = csv.reader(f)
            for row in reader:
                time.sleep(3)
                yangb.param["name"] = row[1]
                yangb.param["hrssCode"] = row[2]
                yangb.param["zipCode"] = row[3]
                yangb.param["address"] = row[4]
                yangb.param["linkMan"] = row[5]
                yangb.param["linkMobile"] = row[6]
                yangb.param["linkIdCode"] = row[7]
                yangb.param["unitedCode"] = row[8]
                # 推送
                # r = requests.post("http://101.37.28.80/kingbao-web-admin/apply/addCert",data=yangb.param,headers=head)
                # if r.status_code == 200:
                #     result = r.json()
                print(row[1])
                if func: func(row)
            print(">>>>>>>>>>>>>>>导入完成!")
            if func: func(None,True)

if __name__ == "__main__":
    yb = yangb()
    yb.username = input("请输入账号:")
    if yb.username and yb.did.get(yb.username):
        pass  
    else:
        print("账号不存在,程序退出!")
        exit()
        
    filepath = input("请输入.csv文件路径:")
    if filepath:
        yb.trans(yb.username,filepath)
