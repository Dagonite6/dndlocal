from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
mapping = {
        "properties":{
            "spells":{
                "type": "nested",
                "properties": {
                    "name":{"type": "nested", "properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "level":{"type": "byte"}}},
                    "text":{"type": "nested", "properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "school":{"type": "nested", "properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "castingTime":{"type": "nested", "properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "range":{"type": "short"},
                    "castingType":{"type": "byte"},
                    "materials":{"type": "nested", "properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "components":{"type": "text"},
                    "duration":{"type": "nested", "properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "classes":{"type": "nested", "properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "source":{"type": "text"},
                }
            }

es.indices.create(index="allspells", mappings=mapping)
