'''
elif
else if 否则如果
if
elif
else
1~20岁 ！
20岁~30岁青春奋斗之时
30~50岁人生最后的奋斗
50~---该养老了！
'''
while(True):
    age1 = input("请输入您的年龄！")
    age = int(age1)
    if age<=20:
        print("现在是读书的最佳时段要好好学习哦！")
    elif age<=30 and age>20:
        print("现在是青春奋斗之时")
    elif age<=50 and age>30:
        print("现在是最后的奋斗！")
    else:
        print("该养老了！")


