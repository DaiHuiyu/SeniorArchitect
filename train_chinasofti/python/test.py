print('hello1');
print('hello2');
print('hello3');
#    print('hello4');
print('hello3hello3hello3hello3hello3hello3hello3hello3hello3\
hello3hello3hello3hello3hello3hello3hello3hello3\
hello3hello3hello3hello3hello3hello3hello3hello3hello3hello3hello3');
# print(b);
a_1 = 1
_q = 2
# 1_a = 3
# if = 4
# print = 10
# print(print)
c = 9999999999999999999999999999999999999999 ** 100
# print(c)

d = 123_456_789
print(d)

c = 0.1 + 0.2
# print(c) # 0.30000000000000004

# s = 'hello'
# s = "helloq"
# s = 'hello"

s = """锄禾日当午，
汗滴禾下土，
谁知盘中餐，
粒粒皆辛苦"""
s = "子曰:\"学而时习之，\n乐呵\\乐呵\"" 
s = '\u0070'
a = 'abc' +'haha' + '哈哈'
a = 123
# print("a : " + a) 

b = 'Hello %s' %'孙悟空'   # Hello 孙悟空
b = 'Hello %s , 你好 %s' %('Tom','孙悟空' )  # Hello Tom , 你好 孙悟空 
b = 'Hello%3s' %'abcdef'   # Helloabcdef
b = 'Hello%3s' %'ab'     # Hello ab   # %3s 字符串的长度限定在 3 个以上，不足 3 个时 以空格替换
b = 'Hello%3.5s' %'bd'   # Hello bd
b = 'Hello%3.5s' %'abcd'   # Helloabcd
b = 'Hello%3.5s' %'abcdef'  # Helloabcde   # %3.5s 字符串的长度限定在 3-5 之间
b = 'Hello%s' %123.456  # Hello123.456  拼接数字也可以
b = 'Hello%f' %123.456  # Hello123.456000  拼接浮点数
b = 'Hello%.2f' %123.456  # Hello123.46  拼接浮点数,保留两个小数点
b = 'Hello%d' %123.456  # Hello123  拼接整数
# print(b)
# print('a = %s'%a)
c = f'hello {a} {b}'
# print(c)

# 创建一个变量来保存你的名字
name = '孙悟空'

#使用四种方式来输出， 欢迎 xxx 光临
# 拼串
print('欢迎 '+name+' 光临!')
#多个参数
print('欢迎',name,'光临!')
#占位符
print('欢迎 %s 光临!'%name)
#格式化字符串
print(f'欢迎 {name} 光临!')

a = 'abc'
a = a * 10
# print(a) 

a = True
a = False
print('a = ', a )
print(1 + True)

b = None
print(b)

c = type('123')
print(c)

print(id('33'))
print(type('125'))

# a = 'hello'
# b = 123
# print(a + b )

# a = True
# 调用int()来将a转换为整型
# int()函数不会对原来的变量产生影响,他是对象转换为指定的类型并将其作为返回值返回。
# a = int(a)
# a = '12.3'
# a = None
# a = int(a)
# print('a = ',a)
# print('a的类型是  ',type(a))

# a = False
# a = float(a)
# print('a = ',a)
# print('a的类型是  ',type(a))

# a = 123
# a = str(a)
# print('a = ',a)
# print('a的类型是  ',type(a))

# True --> 'True'
# False --> 'False'
# 123 --> '123'

# a = False
# a = str(a)
# print('a = '+a)
# print('a的类型是  ',type(a))

# # 创建复数
# z1 = 3 + 4j     # 直接使用字面量
# z2 = complex(3, 4)  # 使用complex()函数
# print(z1)       # 输出: (3+4j)
# print(z2)       # 输出: (3+4j)

# my_list = [1, 2, 3]
# print(id(my_list))  # 输出内存地址
# my_list.append(4)   # 修改列表内容
# print(id(my_list))  # 内存地址不变

# my_dict = {'a': 1, 'b': 2}
# print(id(my_dict))  # 输出内存地址
# my_dict['c'] = 3    # 添加新键值对
# print(id(my_dict))  # 内存地址不变

# # True and True
# result = 1 and 2  # 2
# # True and True
# result = 1 and 0  # 0
# # True and True
# result = 0 and 2  # 0
# print("result = " , result)

# # True or True
# result = 1 or 2  # 1
# # True or False
# result = 2 or 0  # 2
# # False or False
# result = None or 0  # 0
# print("result = " , result)

# result = 1 < 2 < 3  # True
# result = 10 < 20 > 15   # True
# print("result = " , result)

## 循环嵌套练习
### 练习1 ： 打印99乘法表
# i = 0 
# while i < 9 :
#     i +=1
#     j = 0
#     while j < i :
#         j += 1
#         # print("* ")
#         # print(i,'*',j,'=',i * j ,"  ",end = '')  # end = '' 代表不换行
#         print(f"{j}*{i}={i*j}",end = ' ')  # end = '' 代表不换行
#     print()

### 练习2 : 求 100以内的所有的质数
### 默认是质数
# i = 2 # 1不是质数，也不是合数
# while i <= 100 :
# 	flag = True
# 	j = 2 
# 	while j < i :
# 	    # print("* ")
# 	    if i % j == 0 :
# 	    	# print(i," 不是质数",end = '')  # end = '' 代表不换行
# 	    	flag = False
# 	    j += 1
# 	if flag == True :
# 		print(i," 是质数")
# 	# print()
# 	i +=1


# break和continue
 
