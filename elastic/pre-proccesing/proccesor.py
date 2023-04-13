import json
from pprint import pprint
import string

with open("sources/spells.json", "r") as f:
    data = json.load(f)

# initialize proccesed spells dict
allspells = {
    "spells": [],
}

for value in data:
    for spell in data[value]:
        temp_spell = {
            "name": {"en": "", "ru": ""},
            "level": 0,
            "text": {"en": "", "ru": ""},
            "school": 0,
            "castingTime": {"en": "", "ru": ""},
            "range": 0,
            "castingType": 0,
            "materials": {"en": "", "ru": ""},
            "components": [""],
            "duration": {"en": "", "ru": ""},
            "classes": {"en": [""], "ru": [""]},
            "source": "",
        }
        for lang in spell:
            match lang:
                case "en":
                    for name in spell[lang]:
                        match name:
                            case "name":
                                temp_spell["name"]["en"] = str(spell[lang][name])
                            case "level":
                                temp_spell["level"] = int(spell[lang][name])
                            case "text":
                                temp_spell["text"]["en"] = str(spell[lang][name])
                            case "school":
                                match str(spell[lang][name]).lower():
                                    case "abjuration":
                                        temp_spell["school"] = 0
                                    case "alteration":
                                        temp_spell["school"] = 1
                                    case "conjuration":
                                        temp_spell["school"] = 2
                                    case "divination":
                                        temp_spell["school"] = 3
                                    case "enchantment":
                                        temp_spell["school"] = 4
                                    case "illusion":
                                        temp_spell["school"] = 5
                                    case "invocation":
                                        temp_spell["school"] = 6
                                    case "necromancy":
                                        temp_spell["school"] = 7
                            case "castingTime":
                                temp_spell["castingTime"]["en"] = str(spell[lang][name]).lower()
                            case "range":
                                range_string = spell[lang][name]
                                match range_string:
                                    case "Self" | "self":
                                        temp_spell["range"] = 0
                                        temp_spell["castingType"] = 1

                                    case "Unlimited":
                                        temp_spell["range"] = -1
                                        temp_spell["castingType"] = 2

                                    case "Touch" | "touch":
                                        temp_spell["range"] = 0
                                        temp_spell["castingType"] = 3

                                    case "Special":
                                        temp_spell["range"] = 0
                                        temp_spell["castingType"] = 4

                                    case "Sight":
                                        temp_spell["range"] = 0
                                        temp_spell["castingType"] = 5

                                    case _:
                                        if ("Self" in range_string
                                            and "cone" in range_string):
                                            temp_spell["castingType"] = 6
                                            range_int = int("".join(filter(str.isdigit, range_string)))
                                            temp_spell["range"] = range_int

                                        elif ("Self" in range_string
                                            and "radius" in range_string):
                                            temp_spell["castingType"] = 7
                                            range_int = int("".join(filter(str.isdigit, range_string)))
                                            temp_spell["range"] = range_int

                                        elif "cone" in range_string:
                                            temp_spell["castingType"] = 8
                                            range_int = int("".join(filter(str.isdigit, range_string)))
                                            temp_spell["range"] = range_int

                                        elif "radius" in range_string:
                                            temp_spell["castingType"] = 9
                                            range_int = int("".join(filter(str.isdigit, range_string)))
                                            temp_spell["range"] = range_int

                                        elif "line" in range_string:
                                            temp_spell["castingType"] = 10
                                            range_int = int("".join(filter(str.isdigit, range_string)))
                                            temp_spell["range"] = range_int

                                        elif ("Self" in range_string
                                            and "cube" in range_string):
                                            temp_spell["castingType"] = 11
                                            range_int = int("".join(filter(str.isdigit, range_string)))
                                            temp_spell["range"] = range_int

                                        elif "mile" in range_string:
                                            temp_spell["castingType"] = 0
                                            range_int = int("".join(filter(str.isdigit, range_string)))
                                            temp_spell["range"] = range_int * 5280

                                        else:
                                            temp_spell["castingType"] = 0
                                            range_int = int("".join(filter(str.isdigit, range_string)))
                                            temp_spell["range"] = range_int

                            case "materials":
                                temp_spell["materials"]["en"] = str(spell[lang][name])
                            case "components":
                                temp_spell["components"] = spell[lang][name]
                            case "duration":
                                temp_spell["duration"]["en"] = str(spell[lang][name]).lower()
                            case "source":
                                temp_spell["source"] = str(spell[lang][name])

                case "ru":
                    for name in spell[lang]:
                        match name:
                            case "name":
                                temp_spell["name"]["ru"] = spell[lang][name]
                            case "text":
                                temp_spell["text"]["ru"] = str(spell[lang][name])
                            case "materials":
                                temp_spell["materials"]["ru"] = str(spell[lang][name])
                            case "duration":
                                temp_spell["duration"]["ru"] = str(spell[lang][name]).lower()
                            case "castingTime":
                                temp_spell["castingTime"]["ru"] = str(spell[lang][name]).lower()

        allspells["spells"].append(temp_spell)


with open("../proccesed/proccesedSpells.json", "w", encoding="utf-8") as f:
    json.dump(allspells, f, ensure_ascii=False, indent=4)
