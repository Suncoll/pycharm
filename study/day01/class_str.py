"加油"
# 字符串使用
name='hello!'
print(len(name))

# 2  字符串取值  字符串名[索引值】
# 从0开始取
print(name[-1])

# 3 字符串取多个值  切片   字符串名【索引头：索引尾：步长】 步长默认为1
# print(name[1:5:1])   #取头不取尾
# print(name[3:])
# print(name[:3])

print(name[-1:-7:-1])
print(name[::-1])

# 字符串的分割 字符串.split(可以指定切割符号)
# 返回一个列表数据 列表里的子元素都是字符串类型
# 指定的切割符会被切割走
print(name.split("e"))


# 字符串的替换  字符串.replace(指定替换值，新值)
sum='hello'
sum1=sum.replace('h','l')
print(sum1)

# 字符串的去除指定字符  字符串.strip(指定字符）
sum2='hel'
print(sum2.strip("h"))

# 字符串的拼接 + 保证+左右的变量值要一致
a='hello'
b='world'
print(a+b)

# 字符串格式化输出 % format
age=18
name='小恒星'
print('python的{}今年{}'.format(name,age))

# 格式化输出1： format特点 {}用来占位

# 格式化输出2 %  %s字符串  %d数字   %f浮点数
print('python的%s今年%d'%format(name,age))
