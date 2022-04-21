"加油"
# 控制语句  分支 分流  循环语句  for while
# 判断语句  if elif  else
# if 条件语句(比较、逻辑、成员运算、均可）
# 一个条件语句只能有一个if
import random
socre=int(input("输入你的成绩\n"))
if socre<60:
    print("成绩不合格")
elif 60<socre<80:
    print("成绩还可以")
else:
    print("满分")



a=input('输入红灯\n')

if a=='红灯':
    print('停')
else:
    print("走")


print('请问商品的价格')

Q=int(input('请输入商品的价格'))
if Q<50:
    print('没有折扣')
elif 50<=Q<=100:
    price=Q * 0.9
    print(price)


a=random.randint(1,9)
b=int(input("请输入你的数字"))
if a>b:
    print("大于")
elif a==b:
    print("等于")
else:
    print("小于")