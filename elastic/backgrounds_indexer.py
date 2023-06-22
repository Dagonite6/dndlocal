from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
with open("pre-proccesing/proccesed/proccesedBackgrounds.json", "r") as f:
    data = json.load(f)

def gendata():
    for i, background in enumerate(data):
        yield {
            '_index': 'backgrounds',
            '_id': i+1,
            '_source': background
        }


resp = bulk(es, gendata())
print(resp)