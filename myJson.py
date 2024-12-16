import json
import os

#========================================================================================================================================================================================================#

curr_path = "/Users/vincenttainan/Desktop/pythonCSTP"
ex_path = "./jsons/ex_player.json"
list_path = "./resource/player_list.json"
os.chdir(curr_path)
# Since the abs path is greater than 3 layers, path should be written down

#========================================================================================================================================================================================================#

def merge(json1, json2):
    # throwing {json2} into {json1}
    # json1, json2 should both be dictionary
    json1.update(json2)

#========================================================================================================================================================================================================#

def new_player(user_id):
    # adding a new player into list & adding a new player_info file
    # user_id should be a string
    with open(ex_path, 'r') as file:
        data=file.read()
        rfile=json.loads(data)
    
    try:
        with open(list_path, 'r') as file:
            data = file.read()
            player_list = json.loads(data)
    
    except (FileNotFoundError, json.JSONDecodeError):
        player_list = {"user": []}

    if user_id not in player_list["user"]:
        player_list["user"].append(user_id)
        with open(list_path, 'w') as profile:
            json.dump(player_list, profile, indent='\t')

    if not os.path.isfile(f"./resource/{user_id}.json"):
        with open(f"./resource/{user_id}.json", 'w') as profile:
            json.dump(rfile, profile, indent='\t')    

#========================================================================================================================================================================================================#

def get_value(user_id, type_key, key):
    # Getting the value of <user_id> [type_key][key]
    # user_id, type_key, key should all be strings
    if not os.path.isfile(f"./resource/{user_id}.json"):
        new_player(user_id)
        
    with open(f"./resource/{user_id}.json", 'r') as file:
        data = file.read()

    rfile = json.loads(data)

    return rfile[type_key][key]

#========================================================================================================================================================================================================#

def modify_value(user_id, type_key, key, value):
    # !!! there's no method to prevent resource or else from dropping below zero !!!
    # modifying the value of <user_id> [type_key][key] by adding value
    # user_id, type_key, key should all be string
    # value should be a integer
    if not os.path.isfile(f"./resource/{user_id}.json"):
        new_player(user_id)
        
    with open(f"./resource/{user_id}.json", 'r') as file:
        data = file.read()

    rwfile = json.loads(data)
    
    rwfile[type_key][key] += value
    
    with open(f"./resource/{user_id}.json", 'w') as file:
        json.dump(rwfile, file, indent='\t')

    return rwfile[type_key][key]

#========================================================================================================================================================================================================#

def update_all_stamina():
    # restore each player's stamina by 1
    # !!! if someone's name is not in the list, then he cannot get the update !!!
    with open(list_path, 'r') as file:
        data=file.read()
        player_list=json.loads(data)

    for user_id in player_list["user"]:
        if not os.path.isfile(f"./resource/{user_id}.json"):
            new_player(user_id)

        with open(f"./resource/{user_id}.json", 'r') as file:
            data = file.read()

        rwfile = json.loads(data)

        current_stamina = rwfile["stamina"].get("now_stamina", 0)
        max_stamina = rwfile["stamina"].get("max_stamina", 20)
        
        if current_stamina < max_stamina:
                rwfile["stamina"]["now_stamina"] += 1

        with open(f"./resource/{user_id}.json", 'w') as file:
            json.dump(rwfile, file, indent='\t')
