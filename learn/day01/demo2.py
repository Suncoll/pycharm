"加油"

# 列表  索引从0开始
list_name= ['trek', 'cannondale', 'redline', 'specialized']
print(list_name[-1].title())  #访问最后一个元素
learn="我的第一辆自行车"+list_name[0].title()
print(learn)

# 打印
name=['a','a1','hello']
say="你好"
print(name[0]+","+say)
print(name[1]+","+say)
print(name[2]+","+say)

# 修改元素值
list_name[0]='world'
print(list_name)

# 添加元素
list_name.append('city')
print(list_name)

# 指定位置添加元素
list_name.insert(1,'hangzhou')
print(list_name)

# 删除元素 del
del list_name[1]
print(list_name)

# pop删除
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# remove()  删除指定值
motor = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motor)
motor.remove('yamaha')
print(motor)

# 排序 sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 相反排序  reverse=True
cars.sort(reverse=True)
print(cars)

# 临时排序 sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# 列表倒序排列 reverse() 不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序
car=['col','sun','shk','sumny']
car.reverse()
print(car)

# len 读取列表元素个数
print(len(car))

# learn
world=['bmw', 'audi', 'toyota', 'subaru']
print(world)
print(sorted(world))
print(world)
world.sort()
print(world)


# for
pizza=['披萨1','披萨2','披萨3']
for i in pizza:
    print(i)
    print('I like '+i+' pizza')
print('I really love pizza!')

# range
list_sum=list(range(1,11,2))  #打印奇数
print(list_sum)

list_sumone=list(range(1,101))
print(min(list_sumone))
print(max(list_sumone))
print(sum(list_sumone))

# 列表
sum=[a for a in range(1,11) if a%2==0] #取偶数
print(sum)

sum1=[a for a in range(1,11) if a%2==1] #取偶数
print(sum1)

# 切片
sum2=['北京','瑞典','巴黎','冰岛','杭州','西湖']
print(sum2[0:2])
print(sum2[:5]) # 没有指定第一个索引，就从第一个取数
print(sum2[1:]) # 没有指定最后一个索引，就从取到最后
print(sum2[-3:]) # 取最后三个元素值

# 遍历切片
for i in sum2[:3]:
    print('遍历切片名称'+i)

sum3=[10,30,100,50,5]
sum3.sort(reverse=True)
print(sum3)

a=0
for i in sum3[:3]:
    a=a+1
    print('第{0}名得分是{1}'.format(a,i))

# 复制列表 [:]
sumcol=sum3[:]
print(sumcol)

# '''列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。
#  然而，有时候你需要创建一系列不可修 改的元素，元组可以满足这种需求。
#  Python将不能修改的值称为不可变的 不 ，而不可变的列表被称为元组元 。'''

# 元组元素不可修改
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值
charm=(100,300,1000)
for i in charm:
    print(i)

print('\n')
charm=(100,200,100)
for i in charm:

    print(i)
charm=(100,400)
print(charm)

list_col1=[1,3,5]
list_col2=[1,3,5]
if list_col1==list_col2:
    print("=")
else:
    print('!=')


cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# if else
score=int(input('请输入你的成绩\n'))
if score<60:
    print('没有及格')
elif score<80:
    print('及格了但是没有优秀')
elif score>=80:
    print('成绩很优秀')

# 如果你只想执行一个代码块，就使用if-elif-else 结构；如果要运行多个代码块，就使用一系列独立的if 语句。

age=int(input('请输入你的年龄'))
if age<2:
    print("你还是个小孩")
elif 2<=age<13:
    print('蹒跚学步')
elif 13<=age<20:
    print('青少年')
elif 20<=age<60:
    print('中年')


list_name1=['杭州','北京','武汉']
namcol='眉山'
if namcol not in list_name1:
    print('城市')
for i in list_name1:
    print(i+'是美丽的城市')

# 在if 语句中将列表名用在条件表达式中 时，Python将在列表至少包含一个元素时返回True ，并在列表为空时返回False 。

admin_name=['ad','adm','admi','admin','adminn']
for i in admin_name:
    if i=='admin':
        print('“Hello admin, would you liketo seeastatus report?”')
    else:
        print('“Hello Eric, thank you for logging in again”')


print(admin_name)
if admin_name:

else:
    print('“We need to find some users!”')

print(admin_name)
