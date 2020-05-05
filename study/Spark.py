import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import *
import pandas as pd
import numpy as np

conf = pyspark.SparkConf().set('spark.driver.host','127.0.0.1')
sc = pyspark.SparkContext(master='local', appName='myAppName',conf=conf)

sqlContext = SQLContext(sc)

df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferSchema='true')\
    .load('doc_use_log.csv').cache()

df.printSchema()  # header 정보
print(df.count())

# convert the df to tmp table (as if it's in database)
df.registerTempTable("df_tmp")

# extract data from table with sql
df1 = sqlContext.sql("select ismydoc, actiontype, sessionid from df_tmp where ismydoc=true")
df1.show()

sqlContext.sql("select datetime, count(1) from df_tmp group by datetime order by datetime").show()

# Lazy Execution
df2 = sqlContext.sql("select * from df_tmp")

# sessionid, ext 출력 where ext == PDF or DOC, 중복 제거
df2_pdf = df2.select("sessionid", "ext").filter(" ext == 'PDF' or ext = 'DOC'").dropDuplicates().cache()
df2_pdf.show()

# sessionid, datetime 선택? aggregation min(datetime) 이 어떤 역할을 하는지는 모르겠음
df2_min = df2.groupby("sessionid").agg(min("datetime").alias("min_date"))
df2_min.show()

# df2_pdf 에 df2_min의 sessionid 왼쪽 에 join
df2_join = df2_pdf.join(df2_min, "sessionid", "left")
df2_join.show()

