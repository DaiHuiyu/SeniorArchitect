# 显示欢迎信息
print('-' * 20,'欢迎光临《唐僧大战白骨精》','-' * 20)

# 显示游戏身份选择的信息
print('请选择你的身份； ')
print('\t1,唐僧')
print('\t2,白骨精')
# 游戏的身份选择
player_choose = input('请选择[1-2]: ')
# 根据用户的选择来显示不同的提示信息

# 打印一条分割线
print('-' * 66)

# 根据用户的选择来显示不同的提示信息
if player_choose == '1' :
	print('你已经选择唐僧')
elif player_choose == '2' :
	print('你已经选择2，但是强制选择唐僧')
else :
	print('输入有误，强制选择唐僧')

# 进入游戏
# 2、游戏进行 
player_life = 2 # 生命值
player_attack = 2 # 攻击力

boss_life = 10 # 生命值
boss_attack = 10 # 攻击力

# ① 显示玩家的基本信息(攻击力、生命值) 
print(f'唐僧，生命值是{player_life},攻击力是{player_attack}')
# ②显示玩家可以进行的操作: 
# 1、练级 提升玩家的攻击力和生命值 
# 2、打BOSS 玩家对BOSS进行攻击，玩家要攻击BOSS,BOSS对玩家进行反击计算BOSS是否被玩家消灭，玩家是否被BOSS消灭游戏结束 
# 3、逃跑 退出游戏,显示提示信息,游戏结束!
while True :
	# 打印一条分割线
	print('-' * 66)
	print('请选择你要进行的操作')
	print('\t1、练级')
	print('\t2、打BOSS')
	print('\t3、逃跑')
	game_choose = input('请选择的操作 [1-3]')

	# 处理用户的选择
	if game_choose == '1' :
		# 增加玩家的生命值和攻击力
		player_life += 2
		player_attack += 2
		# 显示最新的信息
		print(f'唐僧，恭喜升级了,生命值是{player_life},攻击力是{player_attack}')
	elif game_choose == '2' :
		# 玩家攻击boss
		#减去boss的生命值
		boss_life -= player_attack
		print('唐僧攻击了白骨精')
		#检查boss是否死亡
		if boss_life <= 0 :
		#boss死亡，游戏结束
			print('白骨精死了')
			# 游戏结束
			break
	   # boss反击玩家
		else :
			player_life -= boss_attack
			print('白骨精攻击了唐僧')
		if player_life <= 0 :
			print('唐僧死了')
			# 游戏结束
			break
	elif game_choose == '3' :
    	# 逃跑,退出游戏
	    print('唐僧跑了')		
	    break
	else :
		print('输入有误，请重新输入')