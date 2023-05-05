from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])

mapping = {
        "properties":{
            "equipment":{
                "properties": {
                    "name": {"properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "text": {"properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "props":{"type": "text"},
                    "damageType":{"type": "keyword"},
                    "category": {"type": "keyword"},
                    "typeAdditions": {"type": "keyword"}

                }
            }
        }
}

es.indices.create(index="equipment", mappings=mapping)

