from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
with open("pre-proccesing/proccesed/proccesedRaces.json", "r") as f:
    data = json.load(f)

def gendata():
    for i, race in enumerate(data):
        yield {
            '_index': 'races_en',
            '_id': i+1,
            '_source': race
        }


resp = bulk(es, gendata())
print(resp)