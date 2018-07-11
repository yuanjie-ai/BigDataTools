[<h1 align = "center">:rocket: mmlspark :facepunch:</h1>][0]

---
- add jars
```python
from ispark import SparkStarter
sc, spark = SparkStarter(SPARK_HOME='/home/bigdata/software/spark-2.1.0.7-bin-2.4.0.10').sc_spark
sc.addPyFile('/home/fbidm/mmlspark-0.13.jar')

from mmlspark import LightGBMClassifier
```






---
[0]: https://github.com/Azure/mmlspark
