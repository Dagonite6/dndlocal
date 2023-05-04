from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
with open("pre-proccesing/proccesed/proccesedClassSpells.json", "r") as f:
    data = json.load(f)

for spell in data:
    classes = data[spell]
    query = {
        "match": {
            "name.en": spell
        }
    }
    resp = es.search(index="spells", query=query, source=False)
    if len(resp["hits"]['hits']) > 0:
        spell_id = resp['hits']['hits'][0]['_id']
        body = {
            'classes': classes
        }
        resp = es.update(index="spells", id=spell_id, doc=body)
        print(resp)

