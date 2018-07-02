[<h1 align = "center">:rocket: 描述性统计 :facepunch:</h1>][0]

---
- add jars
```python
from ispark import *
_spark = SparkStarter(SPARK_HOME='/home/bigdata/software/spark-2.1.0.7-bin-2.4.0.10')
sc = _spark.sc
spark = _spark.spark
# spark.conf.set("spark.jars.packages", "Azure:mmlspark:0.13")
sc.addPyFile('/home/fbidm/mmlspark-0.13.jar')


from mmlspark import LightGBMClassifier
```






---
[0]: https://github.com/Azure/mmlspark
