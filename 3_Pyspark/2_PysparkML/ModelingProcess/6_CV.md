```python
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import BinaryClassificationEvaluator

clf = RandomForestClassifier()
grid = ParamGridBuilder().addGrid(clf.maxBins, [32]) \
                         .addGrid(clf.maxDepth, [8]) \
                         .addGrid(clf.impurity, ["gini"]) \
                         .addGrid(clf.numTrees, [100, 200, 500]) \
                         .build()
evaluator = BinaryClassificationEvaluator(metricName='areaUnderROC')

CV = CrossValidator(estimator=clf, estimatorParamMaps=grid, evaluator=evaluator, numFolds=3, seed=0)
cvModel = cv.fit(df.cache())
print(cvModel.avgMetrics[0])
```
