"加油"
# for item in 某个数据类型:(数据类型包括:字符串 列表 元组 字典 集合等）
        #代码块
# for循环的循环次数 有元素的个数决定

sum=0
L=[5,6,7,9,3]
for i in L:
    sum=sum+i
print(sum)

sum1={
    "age":10,
    "sum":1
}
print(sum1.values())  # 获取字典的所有value值
print(sum1.keys())  # 获取字典的所有key值

# range(m,n,k)  取头不取尾

col=0
for i in range(1,101):
    col=col+i
print(col)


L=[[1,2,3,4,5],['CE','CESHI']]
for i in L:
    print(i)
    for a in i:
        print("数字{}".format(a))