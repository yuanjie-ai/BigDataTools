# :rocket: Deploy :facepunch:
---
## IDE spark任务结构
- Data.zip
    - data.csv
    - ...
- MySparkOnline.zip
    - MyPackage
        -  SparkSession
        -  UDF
    - PypiPackage: jieba(举例)
---
## IDE spark-submit
- spark-submit [options] <app jar | python file> [app options]
> spark-submit --help

```python
# -*- coding: utf-8 -*-
import os
import sys
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='This is pyspark task!!!')
parser.add_argument('-n', '--num_executors')
parser.add_argument('-e', '--executor_memory')
parser.add_argument('-p', '--py_files')
parser.add_argument('-m', '--main')
args = parser.parse_args()

def get_args(x, y):
    if x:
        return x
    else:
        return y

num_executors = '--num-executors %s' % get_args(args.num_executors, '10')
executor_memory = '--executor-memory %s' % get_args(args.executor_memory, '20G')
py_files = '--py-files %s' % get_args(args.py_files, args.main)

cmd = \
"source change_spark_version spark-2.1.0 && /home/bigdata/software/spark-2.1.0.7-bin-2.4.0.10/bin/spark-submit \
--master yarn-cluster \
--driver-memory 3G \
--executor-cores 2 \
%s %s %s %s" % (num_executors, executor_memory, py_files, args.main)

os.system(cmd)
```


