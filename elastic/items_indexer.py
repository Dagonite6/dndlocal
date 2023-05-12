from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
with open("pre-proccesing/proccesed/proccesedItems.json", "r") as f:
    data = json.load(f)

def gendata():
    for i, item in enumerate(data):
        yield {
            '_index': 'items',
            '_id': i+1,
            '_source': item
        }

resp = bulk(es, gendata())
print(resp)