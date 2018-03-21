# -*- coding: utf-8 -*-
"""
__title__ = 'spark_init'
__author__ = 'JieYuan'
__mtime__ = '2018/3/16'
"""
import os
import sys
from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *



# 动态分区
# spark.sql("set hive.exec.dynamic.partition.mode = nonstrict")


class Spark:

    def __init__(self, SPARK_HOME="/opt/BigData/spark" , py4j="py4j-0.10.4-src.zip"):
        os.environ["SPARK_HOME"] = SPARK_HOME
        os.environ["PYSPARK_PYTHON"] = os.popen('which python').read().strip()
        sys.path.append("%s/python" % SPARK_HOME)
        sys.path.append("%s/python/lib/%s" % (SPARK_HOME, py4j))

    @property
    def spark(self):
        spark = SparkSession.builder \
            .appName("Yuanjie") \
            .config('log4j.rootCategory', "WARN") \
            .enableHiveSupport() \
            .getOrCreate()
        return spark

    @property
    def sc(self):
        return self.spark.sparkContext















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
