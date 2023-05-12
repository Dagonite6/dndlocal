from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])

mapping = {
        "properties":{
            "spell":{
                "properties": {
                    "race_name": {"type": "keyword"},
                    "speed":{"type": "byte"},
                    "size": {"type": "keyword"},
                    "languages": {"type": "keyword"},

                }
            }
        }
}

es.indices.create(index="races_en", mappings=mapping)

