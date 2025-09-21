##循环语句 
# 练习1： 求100以内所有的奇数之和 

# i = 0
# result = 0 
# while i < 100 :
# 	i += 1
# 	if i % 2 != 0 :
# 		result += i 
# print('result = ',result)


# 练习2： 求100以内所有7的倍数之和，以及个数 

# i = 0
# result = 0 
# num = 0
# while i < 100 :
# 	i += 1
# 	if i % 7 == 0 :
# 		num += 1
# 		result += i 
# print('num = ',num)
# print('result = ',result)

# 练习3： 水仙花数是指一个n位数(n>=3 ) ,它的每个位上的数字的n次幂之和等于它本身(例如: 1**3 +5**3+ 3**3 = 153)。 
# 求1000以内所有的水仙花数 

# i = 100
# while i < 1000 :
# 	# 假设 i的百位数为 a , 十位数为 b , 个位数为 c
# 	a = i // 100
# 	b = i // 10 % 10 
# 	c = i % 10
# 	if (a ** 3 + b ** 3 + c ** 3) == i :
# 		print('水仙花数: ', i)
# 	i += 1


# 练习4： 获取用户输入的任意数，判断其是否是质数。质数是只能被1和它自身整除的数，1不是质数也不是合数。
num = int(input('请输入一个任意大于1的整数:'))
i = 2
# 创建一个变量，用来记录num是否为质数，num默认是质数
flag = True
while i < num :
	if num % i == 0 :
		flag = False
	i += 1
if flag :
	print(num,'是质数')
else :
	print(num,'不是质数')
