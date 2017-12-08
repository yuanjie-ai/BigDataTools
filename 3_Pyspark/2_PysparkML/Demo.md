# Spark数据挖掘套路：RF示例

标签（空格分隔）： Spark 机器学习 建模流程

---

# 依赖包
```

import pandas as pd
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.tuning import ParamGridBuilder,CrossValidator,TrainValidationSplit
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
```

# 样例数据
```
df = pd.read_csv('/home/fbidm/.yuanjie/Python/iris.csv')
data = spark.createDataFrame(df)
# data.replace()也可以
stringIndexer = StringIndexer(inputCol="Species", outputCol="label", handleInvalid='error')
data = stringIndexer.fit(data).transform(data).drop("Species")
# 修改列名
for i,j in zip(data.columns[:4],list("abcd")):
    data  = data.withColumnRenamed(i,j)

vecAssembler = VectorAssembler(inputCols=data.columns[:4], outputCol="features")
data = vecAssembler.transform(data)

train,test = data.randomSplit([0.8,0.2])
train.cache();test.cache()
train.show(5)
```
```
+---+---+---+---+-----+-----------------+
|  a|  b|  c|  d|label|         features|
+---+---+---+---+-----+-----------------+
|4.6|3.1|1.5|0.2|  2.0|[4.6,3.1,1.5,0.2]|
|4.7|3.2|1.3|0.2|  2.0|[4.7,3.2,1.3,0.2]|
|5.0|3.6|1.4|0.2|  2.0|[5.0,3.6,1.4,0.2]|
|5.1|3.5|1.4|0.2|  2.0|[5.1,3.5,1.4,0.2]|
|5.4|3.9|1.7|0.4|  2.0|[5.4,3.9,1.7,0.4]|
+---+---+---+---+-----+-----------------+
only showing top 5 rows
```
# 选择最优模型
- estimator
- evaluator
- estimatorParamMaps
```
rf = RandomForestClassifier()
grid = ParamGridBuilder().addGrid(rf.maxBins,[24,28,32,36]) \
                         .addGrid(rf.maxDepth,[4,6,8,10]) \
                         .addGrid(rf.impurity,["entropy","gini"]) \
                         .addGrid(rf.numTrees,[15,20,25,30]) \
                         .build()
evaluator = MulticlassClassificationEvaluator(metricName = 'f1') # f1|weightedPrecision|weightedRecall|accuracy
# evaluator = BinaryClassificationEvaluator(metricName = 'areaUnderROC') # areaUnderROC|areaUnderPR

```

- CrossValidator
```
cv = CrossValidator(estimator=rf, estimatorParamMaps=grid, evaluator=evaluator,numFolds = 3)
cvModel = cv.fit(train)
 
# avgMetrics与getEstimatorParamMaps一一对应
cvModel.avgMetrics
cvModel.getEstimatorParamMaps()

cvModel.getEvaluator().extractParamMap()
cvModel.getEvaluator().isLargerBetter # 评估指标是否越大越好

cvModel.bestModel.transform(train).show(truncate =False)

evaluator.evaluate(cvModel.transform(test))
```

- TrainValidationSplit
> 类似于cv，不过只选择一次
```
tvs = TrainValidationSplit(estimator=rf, estimatorParamMaps=grid, evaluator=evaluator, trainRatio = 0.75)
tvsModel = tvs.fit(train)

evaluator.evaluate(tvsModel.transform(test))
```
---
# 提交任务
```
spark-submit --master yarn-cluster xx.py
```
