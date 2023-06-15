from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])

res = es.get(index="races_en", id=1)
print(type(res['_source']))