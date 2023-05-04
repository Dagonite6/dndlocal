from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
with open("proccesed/proccesedSpells.json", "r") as f:
    data = json.load(f)

spellsList = data["spells"]

def gendata():
    for i, spell in enumerate(spellsList):
        yield {
            '_index': 'spells',
            '_id': i+1,
            '_source': spell
        }

resp = bulk(es, gendata())
print(resp)