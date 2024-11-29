import random 
import time

def get_rand(a, b):
	#隨機在a,b間(含a,b)取得一數，回傳一數
	random.seed(time.time())
	return random.randint(a, b)
