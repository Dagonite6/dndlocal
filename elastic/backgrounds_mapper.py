from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])

mapping = {
        "properties":{
            "backgrounds":{
                "properties": {
                    "name": {"type": "keyword" },
                    "proficiencies": {"type": "text"},
                }
            }
        }
}

es.indices.create(index="backgrounds", mappings=mapping)

