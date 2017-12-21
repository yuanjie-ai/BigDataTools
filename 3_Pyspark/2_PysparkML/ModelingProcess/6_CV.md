<h1 align = "center">:rocket: 交叉验证 :facepunch:</h1>

---

```python
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import BinaryClassificationEvaluator

clf = RandomForestClassifier()
grid = ParamGridBuilder().addGrid(clf.maxDepth, [8]) \
                         .addGrid(clf.impurity, ["gini"]) \
                         .addGrid(clf.numTrees, [100, 200, 500]) \
                         .build()
evaluator = BinaryClassificationEvaluator(metricName='areaUnderROC')

cv = CrossValidator(estimator=clf, estimatorParamMaps=grid, evaluator=evaluator, numFolds=3, seed=0)
cvModel = cv.fit(df.cache())
print(cvModel.avgMetrics[0])
```
