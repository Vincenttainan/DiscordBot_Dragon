import random 
import time

def get_rand(a, b):
	#隨機在a,b間(含a,b)取得一數，回傳一數
	random.seed(time.time())
	return random.randint(a, b)

def set_chance(weight: list, options: list = []):
	# 以設定好的權重進行抽取
	if len(options) != len(weight):
		options = range(1, len(weight)+1)

	random.seed(time.time())
	return random.choices(options, weight)[0]
