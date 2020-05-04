import datetime
from elasticsearch import Elasticsearch


def insertData():
    es = Elasticsearch('[localhost]:9200')

    index = "product_list"

    doc = {
        "category": "shirt",
        "price": 16700,
        "@timestamp": datetime.datetime.now()
    }
    es.index(index="product_list", doc_type="_doc", body=doc)


def searchAPI():
    es = Elasticsearch('[localhost]:9200')

    index = "product_list"
    body = {
        "query": {
            "match_all": {}
        }
    }
    res = es.search(index=index, body=body)
    print(type(res))
    print(len(res['hits']['hits']))
    for item in res['hits']['hits']:
        print(item['_source'])


#insertData()
searchAPI()