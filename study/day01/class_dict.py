"加油"
# 字典可以存任何数据类型
# 存储 key -vlalue
# 可以存在空字典   无序的
# 字典的key必须是唯一的

a={
    "key":1,
    "age":10,
    "socer":[1,2,3,4]
}

# 字典取值 :  字典[key]
print(a["key"])

# 删除 pop(key) 指明删除的值
res=a.pop("socer")
print(res)

# 新增  a[key]=value   字典中不存在的key
a['测试']=1
print(a)

# 修改  a[已存在的key]=新value  字典中已存在的key
a['key']='测试'
print(a)