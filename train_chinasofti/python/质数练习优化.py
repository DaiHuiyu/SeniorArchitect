from time import *
# 优化前: 10000个数 程序执行花费了:  23.15923047065735 秒
# 第一次优化:  10000个数 程序执行花费了:  10.4611337184906 秒
# 第二次优化:  10000个数 程序执行花费了:  7.4611337184906 秒
# 注意：print(i," 是质数") 耗时严重
begin = time() # 返回的单位是秒
## 默认是质数
i = 2 # 1不是质数，也不是合数
while i <= 100000 :
  flag = True
  j = 2 
  # while j < i :
  while j <= i ** 0.5 : # 第二次优化
      # print("* ")
      if i % j == 0 :
          # print(i," 不是质数",end = '')  # end = '' 代表不换行
          flag = False
          # 第一次优化: 一旦进入判断，则证明i一定不是质数，此时内层循环没有继续执行的必要
          # 使用 break 来退出内层循环
          break
      j += 1
  if flag == True :
      # print(i," 是质数")
      pass
  # print()
  i +=1 
end = time() 
print("程序执行花费了: ",end - begin,"秒")