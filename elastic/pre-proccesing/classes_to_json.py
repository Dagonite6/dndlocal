import json

with open("proccesed/indexes.json", "r") as f:
    indexes = json.load(f)

results = []

template = '<option value="1">Dwarf</option>'

for clas in indexes['classes']:
    option = f'<option value="{clas}">{indexes["classes"][clas]["en"]}</option>'
    results.append(option)

html = "\n".join(results)

with open("proccesed/class_data.html", "w", encoding="utf-8") as f:
    f.write(html)