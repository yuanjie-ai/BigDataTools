<h1 align = "center">:rocket: 交叉验证 :facepunch:</h1>

---

```python
# 实例
df = spark.table('fbidm.yuanjie_train_data_20180108').cache()

from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import BinaryClassificationEvaluator

clf = RandomForestClassifier()
grid = ParamGridBuilder().addGrid(clf.maxDepth, [8]) \
                         .addGrid(clf.impurity, ["gini"]) \
                         .addGrid(clf.numTrees, [100]) \
                         .build()
evaluator = BinaryClassificationEvaluator(metricName='areaUnderROC')

cv = CrossValidator(estimator=clf, estimatorParamMaps=grid, evaluator=evaluator, numFolds=3, seed=0)
cvModel = cv.fit(df)
deploy_date = '20180108'
cvModel.bestModel.write().overwrite().save('/user/fbidm/modelresult/model_%s.model' % deploy_date)
print(cvModel.avgMetrics)
```
