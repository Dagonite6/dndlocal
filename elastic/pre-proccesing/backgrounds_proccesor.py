import json
from pprint import pprint

with open("sources/backgrounds.json", "r") as f:
    data = json.load(f)

proccesed = []

for key in data:
    background = {}
    background['name'] = key['name'].title()
    background['proficiencies'] = []
    for prof in key["skillProficiencies"][0]:
        background["proficiencies"].append(prof.title())
    background["equipment"] = {"base": []}
    for item in key["startingEquipment"]:
        for group in item:
            if group == "_":
                for equip in item[group]:
                    temp = {}
                    if not isinstance(equip, dict ):
                        temp["name"] = equip.title()
                    if "item" in equip:
                        temp["name"] = equip["item"].title()
                    if "special" in equip:
                        temp["name"] = equip["special"].title()
                    if "quantity" in equip:
                        temp["quantity"] = equip["quantity"]
                    if "containsValue" in equip:
                        temp["value"] = equip["containsValue"] 
                    if "equipmentType" in equip:
                        temp["equipmentType"] = equip["equipmentType"] 

                    background["equipment"]["base"].append(temp)
            else:
                if not "choice" in background["equipment"]: 
                    background["equipment"]["choice"] = []
                for choice in item[group]:
                    temp2 = {}
                    if "item" in choice:
                        temp2["name"] = choice["item"].title()
                    if "special" in choice:
                        temp2["name"] = choice["special"].title()
                    if "displayName" in choice:
                        temp2["name"] = choice["displayName"].title()
                    if "quantity" in choice:
                        temp2["quantity"] = choice["quantity"]
                    if "containsValue" in choice:
                        temp2["value"] = choice["containsValue"]  
                    if "equipmentType" in choice:
                        temp2["equipmentType"] = choice["equipmentType"]
                    background["equipment"]["choice"].append(temp2)      
    background["content"] = {"title": key["entries"][1]["name"]}
    background["content"]['text'] = key["entries"][1]["entries"]
    proccesed.append(background)


with open("proccesed/proccesedBackgrounds.json", "w", encoding="utf-8") as f:
    json.dump(proccesed, f, ensure_ascii=False, indent=4)