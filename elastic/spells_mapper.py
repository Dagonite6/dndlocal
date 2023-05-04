from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])

mapping = {
        "properties":{
            "spell":{
                "properties": {
                    "name": {"properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "level":{"type": "byte"},
                    "text":{"properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "school": {"properties": {"en": {"type": "keyword"}, "ru": {"type": "keyword"}}},
                    "castingTime": {"properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "range":{"type": "short"},
                    "castingType":{"type": "byte"},
                    "materials": {"properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "components":{"type": "text"},
                    "duration": {"properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "classes":{"type": "short"},
                    "source":{"type": "keyword"},
                }
            }
        }
}

es.indices.create(index="spells", mappings=mapping)

