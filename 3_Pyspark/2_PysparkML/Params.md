
```python
# rf
params = dict(featuresCol="features",
              labelCol="label", 
              predictionCol="prediction",
              probabilityCol="probability", 
              rawPredictionCol="rawPrediction", 
              maxDepth=8,
              numTrees=100,
              maxBins=10,
              impurity="gini",
              maxMemoryInMB=2560, 
              cacheNodeIds=True,
              seed=0)
```

```python
# gbdt
params = dict(featuresCol="features",
              labelCol="label",
              predictionCol="prediction",
              maxDepth=5,
              maxBins=32,
              minInstancesPerNode=1,
              minInfoGain=0.0,
              maxMemoryInMB=256,
              cacheNodeIds=False,
              checkpointInterval=10,
              lossType="logistic",
              maxIter=20,
              stepSize=0.1,
              seed=0,
              subsamplingRate=1.0)
```

```python
# als
params = dict(rank=10,
              maxIter=10,
              regParam=0.1,
              numUserBlocks=10,
              numItemBlocks=10,
              implicitPrefs=False,
              alpha=1.0,
              userCol="user",
              itemCol="item",
              ratingCol="rating",
              nonnegative=False,
              seed=0)
```
