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
```
# -*- coding: utf-8 -*-
import os
cmd = \
"source change_spark_version spark-2.1.0 && /home/bigdata/software/spark-2.1.0.7-bin-2.4.0.10/bin/spark-submit \
--master yarn-cluster \
--num-executors 40 \
--executor-memory 10G \
--executor-cores 2 \
--driver-memory 3G \
--py-files MySparkOnline.zip,Data.zip "                          # 注意空格

os.system(cmd + '__main__.py')
```


