import json
import re

with open("sources/items.json", "r") as f:
    data = json.load(f)

data_as_string = json.dumps(data)
data_as_string = re.sub(r'<a\s+(?:[^>]*?\s+)?href=(["\'])(?:\\\1|.)*?\1[^>]*>|<\/a>', '', data_as_string)

data_as_json = json.loads(data_as_string)

results = []

for item in data_as_json:
    item['en'].pop('source')
    item['en']['category'] = item['en'].pop('type')
    en_name = item['en'].pop('name').title()
    ru_name = item['ru'].pop('name').title()
    en_text = item['en'].pop('text').title()
    ru_text = item['ru'].pop('text').title()
    en_attunement = ''
    ru_attunement = ''
    en_typeAdditions = ''
    ru_typeAdditions = ''
    if "attunement" in item['en']:
        en_attunement = item['en'].pop('attunement').title()
    if "attunement" in item['ru']:
        ru_attunement = item['ru'].pop('attunement').title()
    if 'typeAdditions' in item['en']:
        en_typeAdditions = item['en'].pop('typeAdditions').title()
    if 'typeAdditions' in item['ru']:
        ru_typeAdditions = item['ru'].pop('typeAdditions').title()
    proccessed = item['en']
    proccessed['name'] = {'en': en_name, 'ru': ru_name}
    proccessed['text'] = {'en': en_text, 'ru': ru_text}
    proccessed['attunement'] = {'en': en_attunement, 'ru': ru_attunement}
    proccessed['typeAdditions'] = {'en': en_typeAdditions, 'ru': ru_typeAdditions}

    results.append(proccessed)

with open("proccesed/proccesedItems.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)