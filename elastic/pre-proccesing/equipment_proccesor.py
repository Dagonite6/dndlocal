import json

with open("sources/equipment.json", "r") as f:
    data = json.load(f)

proccesed = []

for key in data:
    key['en'].pop('source', None)
    key['en']['img'] = key['en']['img'].lower()
    key['en']['cost'] = key['en'].pop('coast', None)
    key['en']['category'] = key['en'].pop('type', None)
    if 'typeAdditions' in key['en']:
        key['en']['typeAdditions'] = key['en'].pop('typeAdditions', None).replace('(','').replace(')','').title()
    en_name = key['en'].pop('name', None).title()
    ru_name = key['ru'].pop('name', None).title()
    en_text = key['en'].pop('text', None).title()
    ru_text = key['ru'].pop('text', None).title()
    key = key['en']
    key['name'] = {'en': en_name, 'ru': ru_name}
    key['text'] = {'en': en_text, 'ru': ru_text}
    proccesed.append(key)

with open("proccesed/proccesedEquipment.json", "w", encoding="utf-8") as f:
    json.dump(proccesed, f, ensure_ascii=False, indent=4)