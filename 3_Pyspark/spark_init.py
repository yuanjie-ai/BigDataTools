# -*- coding: utf-8 -*-
"""
__title__ = 'spark_init'
__author__ = 'JieYuan'
__mtime__ = '2018/3/16'
"""
import os
from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Path for spark source folder
os.environ["PYSPARK_PYTHON"]="/algor/yuanjie/intel/intelpython3/bin/python"
os.environ['SPARK_HOME'] = "/opt/BigData/spark"

# # Path for pyspark and py4j
# sys.path.append("/opt/BigData/spark/python")
# sys.path.append("/opt/BigData/spark/python/lib/py4j-0.10.4-src.zip")

## You might need to enter your local IP
# os.environ['SPARK_LOCAL_IP']="192.168.2.138"

## remote
# spark = SparkSession.builder \
#     .appName("Yuanjie") \
#     .config('log4j.rootCategory', "WARN") \
#     .enableHiveSupport() \
#     .getOrCreate()

## local
spark = SparkSession.builder \
    .master("local") \
    .appName("Yuanjie") \
    .getOrCreate()

sc = spark.sparkContext

# 动态分区
# spark.sql("set hive.exec.dynamic.partition.mode = nonstrict")
















SPARK = \
    '''
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /___/ .__/\_,_/_/ /_/\_\    >>>https://github.com/Jie-Yuan
          /_/

    '''
if __name__ == '__main__':
    print('It is main!!!')
else:
    print(SPARK)
