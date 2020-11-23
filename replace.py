import json
def replace_acro(acro):
    with open("main_final.json", "r") as read_file:
        data = json.load(read_file)
    
    if acro in data:
        return data[acro]
    else:
        return -1