import pyspark
from flask import Blueprint
from pyspark.sql import SQLContext


conf = pyspark.SparkConf().set('spark.driver.host', '127.0.0.1')
sc = pyspark.SparkContext(master='local', appName='myAppName', conf=conf)
sqlContext = SQLContext(sc)

spark = Blueprint('spark', __name__)


@spark.route('/sparkTest')
def sparkTest():
    df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferSchema='true') \
        .load('study/doc_use_log.csv').cache()

    df.printSchema()  # header 정보
    print(df.count())

    return df.show()


@spark.route('/sparkES')
def sparkES():
    '''df = sqlContext.read.format("org.elasticsearch.spark.sql").option("es.nodes", "localhost:9200").option(
        "es.nodes.discovery", "true").load("product_list/_doc")
    df.registerTempTable("tab")ㅏ

    output = sqlContext.sql("SELECT distinct request FROM tab")
    output.show()
    '''
    # 안된다. elasticsearch.spark 가 없나본데.. 또 설치해야하나
    return "OK"
