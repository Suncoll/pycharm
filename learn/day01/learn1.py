"加油"

current_users=['current_users0', 'current_users1', 'current_users2', 'current_users3', 'current_users4']
# for i in range(0,5):
#     col="current_users"+str(i)
#     current_users.append(col)
# print(current_users)
new_users=['current_users0', 'current_users1', 'current_users2', 'current_users30', 'current_users40']

for i in new_users:
    if i in current_users:
        print(i+'被引用')
    else:
        print(i+'没有被引用')

list_sum=list(range(1,10))
for i in list_sum:
    if i==1:
        print('\n')
        print(str(i)+'st')
    elif i==2:
        print('\n')
        print(str(i)+'nd')
    elif i==3:
        print('\n')
        print(str(i)+'rd')
    else:
        print('\n')
        print(str(i)+'th')
    # print(i)

# 字典
city={"1":"武汉","2":"北京"}
print(city["1"])
city['3']='杭州'
print(city)
city['3']='西湖'
print(city)
del city['2']
print(city)


name={
    "1":"col",
    "2":"26",
    "3":"北京"
}
print(name['1']+name['2']+name['3'])

for v in city.values():
    print(v)


langue={
    "1":"1",
    "2":"2",
    "3":"2",
    "4":"3"
}
for i in sorted(set(langue.values())): # set集合对值去重
    print(i)

city1={
    "中国":"黄河",
    "英国":"巴黎",
    "nile":"egypt"
}

for i in city1.values():
    print(i+'The Nileruns throughEgypt')


name1={
    "1":"中国",
    "2":"英国",
    "3":"德国"
}

name2={
    "1":"中国",
    "2":"英国",
    "4":"德国"
}
for i in name1.keys():
    if i in name2.keys():
        print("调查了")
    else:
        print("去调查")

name={
    'tom':[1,2,3],
    'jen':[4],
    'erl':[11,14]
}
for k,v in name.items():
    print('\n名字'+k+'数字')
    for l in v:
        print("数字是"+str(l))

prompt = "\nTell me something, and I will repeat it back to"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)