#coding:utf-8
from pymongo import MongoClient
from datetime import datetime
from hashlib import md5
conn = MongoClient()
db = conn.interactive

def form_data():
    data = {'info': [{"数量": '3',"物品":'soap',"经办人": 'jack', '交通':'walk','web_id':1},
                   {"物品": 'bow', "数量": '2', "经办人": 'mary', '交通':'bike','web_id':2},
                   {"物品": 'noodle', "数量": '5', "经办人": 'mary', '交通': 'car','web_id':3}],
            "user":'laobzhang',
            'key': ['数量', '物品', '经办人', '交通']}
    db.info.insert(data)

{"数量": '4',"物品":'chopstick',"经办人": 'jack', '交通':'walk','web_id':4}

def get_data(user = 'laobzhang'):
    return db.info.find_one(dict(user=user))


if __name__ == '__main__':
    form_data()








