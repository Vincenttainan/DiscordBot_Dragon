import json
import os

path = "/Users/vincenttainan/Desktop/pythonCSTP"
os.chdir(path)
# Since the abs path is greater the 3 layers, path should be written down

def merge(json1, json2):
    # throwing json2 into json1
    # json1, json2 should both be dictionary
    json1.update(json2)

def new_player(user_id):
    # adding a new player into resource
    # user_id should be a string
    with open('./jsons/ex_player.json', 'r') as file:
        data=file.read()
        rfile=json.loads(data)

    rfile[user_id] = rfile.pop("IDwwwwwwwwwwwwwwwwwwID")

    with open('./resource/player.json', 'w+') as file:
        old_data=file.read()
        old_file=json.loads(data)
        merge(rfile,old_file)
        json.dump(rfile, file, indent=4)
