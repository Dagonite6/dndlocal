from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
with open("pre-proccesing/proccesed/proccesedEquipment.json", "r") as f:
    data = json.load(f)

def gendata():
    for i, equipment in enumerate(data):
        yield {
            '_index': 'equipment',
            '_id': i+1,
            '_source': equipment
        }


resp = bulk(es, gendata())
print(resp)