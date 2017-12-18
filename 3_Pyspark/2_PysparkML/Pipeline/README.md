```python
def ml_pipline_preprocessing(df, _id='id', _label='label'):
    id_label = [_id, _label]
    strCol = [i[0] for i in df.dtypes if i[1] == 'string' and i[0] not in id_label]
    str2num_ls = [StringIndexer(inputCol=i, outputCol="_" + i, handleInvalid='skip') for i in strCol]
    vectorAssembler = VectorAssembler(inputCols=[i for i in df.columns if i not in id_label + strCol],
                                      outputCol='features')
    stages = str2num_ls + [vectorAssembler]
    return Pipeline(stages=stages)
```
# cv=1
```python
# cv
clf = RandomForestClassifier()
grid = ParamGridBuilder().addGrid(clf.maxBins, [32]) \
                         .addGrid(clf.maxDepth, [8]) \
                         .addGrid(clf.impurity, ["gini"]) \
                         .addGrid(clf.numTrees, [100, 200, 500]) \
                         .build()
evaluator = BinaryClassificationEvaluator(metricName='areaUnderROC')
cv = CrossValidator(estimator=clf, estimatorParamMaps=grid, evaluator=evaluator, numFolds=3, seed=0)
cvModel = cv.fit(pipline_model.transform(df).cache())
print(cvModel.avgMetrics[0])
```

```python
# cv
clf = RandomForestClassifier()
grid = ParamGridBuilder().addGrid(clf.maxBins, [32]) \
                         .addGrid(clf.maxDepth, [8]) \
                         .addGrid(clf.impurity, ["gini"]) \
                         .addGrid(clf.numTrees, [100, 200, 500]) \
                         .build()
evaluator = BinaryClassificationEvaluator(metricName='areaUnderROC')
val = TrainValidationSplit(estimator=clf, estimatorParamMaps=grid, evaluator=evaluator, trainRatio=0.75, seed=0)
val_model = val.fit(pipline_model.transform(df).cache())
print(cvModel.avgMetrics[0])
```
