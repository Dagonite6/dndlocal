import json

with open("proccesed/proccesedBackgrounds.json", "r") as f:
    bgs = json.load(f)

results = []

template = '<option value="1">Dwarf</option>'

for i, bg in enumerate(bgs):
    option = f'<option value="{i+1}">{bg["name"]}</option>'
    results.append(option)

html = "\n".join(results)

with open("proccesed/bgs_data.html", "w", encoding="utf-8") as f:
    f.write(html)