'''
一个类储存用户的数据一个类用来保留
'''
class userdata:#父类
    name = "yixuan"
    age = 12
    phone="888888"
class user(userdata):#子类
    pass
us = user
print(us.name)