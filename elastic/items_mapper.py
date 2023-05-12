from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])

mapping = {
        "properties":{
            "equipment":{
                "properties": {
                    "name": {"properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "text": {"properties": {"en": {"type": "text"}, "ru": {"type": "text"}}},
                    "categoty": {"type": "keyword"},
                    "attunement": {"properties": {"en": {"type": "keyword"}, "ru": {"type": "keyword"}}},
                    "typeAdditions": {"properties": {"en": {"type": "keyword"}, "ru": {"type": "keyword"}}},

                }
            }
        }
}

es.indices.create(index="items", mappings=mapping)

