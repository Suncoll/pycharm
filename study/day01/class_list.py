"加油"
# 1  可以存放空列表 a=[]
# 2 列表里面可以存放任何数据类型
# 3 列表里面的元素， 根据逗号来分割


a=[0,1,2,3,4,5,6,7,8,9,10]
print(a[::2])   #取偶数位
print(a[::3])

# 列表增加数据    append
a.append(['测试','测试1'])
print(a)

# insert 指定位置添加数据
a.insert(2,'moick')
print(a)

# 删除 pop()  默认删除最后一个元素
# a.remove(1) 指定删除某个值
a.pop()
print(a)
a.remove(3)
print(a)

# 修改  a[索引值]=新值
a[2]=1
print(a)