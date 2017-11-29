#coding:utf-8
from pymongo import MongoClient
from datetime import datetime
from hashlib import md5
conn = MongoClient()
db = conn.interactive

def form_data():
    '''
    { "_id" : ObjectId("5a1e2b0c421aa91505202447"), "info" : [ { "物品" : "soap", "交通" : "walk", "web_id" : 1, "数量" : "3", "经办人" : "jack" }, { "物品" : "bow", "交通" : "bike", "web_id" : 2, "数量" : "2", "经办人" : "mary" }, { "物品" : "noodle", "交通" : "car", "web_id" : 3, "数量" : "5", "经办人" : "mary" }, { "数量" : "4", "物品" : "chopstick", "经办人" : "jack", "交通" : "walk", "web_id" : 5 }, { "数量" : "7", "物品" : "brush", "经办人" : "jack", "交通" : "walk", "web_id" : 6 }, { "数量" : "4", "物品" : "computer", "经办人" : "lily", "交通" : "subway", "web_id" : 7 } ], "user" : "laobzhang", "key" : [ "数量", "物品", "经办人", "交通" ] }
    :return:
    '''
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








