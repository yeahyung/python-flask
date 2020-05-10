from flask import Blueprint
import datetime
from elasticsearch import Elasticsearch


elastic = Blueprint('elastic', __name__)
es = Elasticsearch('[localhost]:9200')
index = "product_list"


# index : product_list, type : _doc
@elastic.route('/putData')
def putData():
    doc = {
        "category": "t-shirt",
        "price": 16700,
        "@timestamp": datetime.datetime.now()
    }
    es.index(index="product_list", doc_type="_doc", body=doc)

    return "OK"


@elastic.route('/searchData')
def searchData():
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

    return res

