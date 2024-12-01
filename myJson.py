import json
import os

#========================================================================================================================================================================================================#

curr_path = "/Users/vincenttainan/Desktop/pythonCSTP"
ex_path = "./jsons/ex_player.json"
resource_path = "./resource/player.json"
os.chdir(curr_path)
# Since the abs path is greater the 3 layers, path should be written down

#========================================================================================================================================================================================================#

def merge(json1, json2):
	# throwing {json2} into {json1}
	# json1, json2 should both be dictionary
	json1.update(json2)

#========================================================================================================================================================================================================#

def new_player(user_id):
	# adding a new player into resource
	# user_id should be a string
	with open(ex_path, 'r') as file:
		data=file.read()
		rfile=json.loads(data)

	rfile[user_id]=rfile.pop("IDwwwwwwwwwwwwwwwwwwID")

	try:
		with open(resource_path, 'r') as file:
			old_data=file.read()
			if old_data:
				old_file = json.loads(old_data)
			else:
				old_file = {}

	except(FileNotFoundError, json.JSONDecodeError):
		old_file={}

	merge(old_file, rfile)

	with open(resource_path, 'w') as file:
		json.dump(old_file, file, indent=4)


#========================================================================================================================================================================================================#

def get_value(user_id, type_key, key):
	# getting the value of <user_id> [type_key][key]
	# user_id, type_key, key should all be string
	with open(resource_path, 'r') as file:
		data=file.read()
		rfile=json.loads(data)
	return rfile[user_id][type_key][key]

#========================================================================================================================================================================================================#

def modify_value(user_id, type_key, key, value):
	# modifying the value of <user_id> [type_key][key] by adding value
	# user_id, type_key, key should all be string
	# value should be a integer
	with open(resource_path, 'r') as file:
		data=file.read()
		rwfile=json.loads(data)
	
	if user_id not in rwfile:
		new_player(user_id)
		with open(resource_path, 'r') as file:
			data=file.read()
			rwfile=json.loads(data)
	
	rwfile[user_id][type_key][key] += value
	
	with open(resource_path, 'w') as file:
		json.dump(rwfile, file, indent=4)








