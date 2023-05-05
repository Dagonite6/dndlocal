import json
from pprint import pprint

with open("sources/classSpells.json", "r") as f:
    data = json.load(f)

with open("proccesed/indexes.json", "r") as f:
    indexes = json.load(f)

spells_results = {}

def add_result(title, spell):
    if spell in spells_results:
        if not title in spells_results[spell]:
            spells_results[spell].append(title)
    else:
        spells_results[spell] = [title]

for clas in data:
    for attr in data[clas]:
        if attr == 'title':
            title = data[clas][attr]['en']
        if attr == 'spells':
            for spell in data[clas][attr]:
                add_result(title, spell.title())
        if attr == 'subclasses':
            for subclass in data[clas][attr]:
                title = subclass['title']['en']
                for spell in subclass['spells']:
                    add_result(title, spell.title())

for spell in spells_results:
    for i, title in enumerate(spells_results[spell]):
        for index in indexes['classes']:
            if title == indexes['classes'][index]['en']:
                spells_results[spell][i] = int(index)
            

with open("proccesed/proccesedClassSpells.json", "w", encoding="utf-8") as f:
    json.dump(spells_results, f, ensure_ascii=False, indent=4)