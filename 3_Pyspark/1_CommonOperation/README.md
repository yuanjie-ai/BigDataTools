# :rocket: 常用操作 :facepunch:
---
- StringIndexer
```
test = spark.range(5)
model = StringIndexer(inputCol='id',outputCol='indexed_id').fit(test)
test2 = model.transform(test)
```
- IndexToString(StringIndexer反向操作)
```
m =IndexToString(inputCol='indexed_id',outputCol='id_old',labels=np.array(['0','1','2','a','b']))
m.transform(test2).show()
```
```
+---+----------+------+
| id|indexed_id|id_old|
+---+----------+------+
|  0|       2.0|     2|
|  1|       1.0|     1|
|  2|       3.0|     a|
|  3|       4.0|     b|
|  4|       0.0|     0|
+---+----------+------+
```
```
# freqItems
df = spark.createDataFrame([(1, 2, 3) if i % 2 == 0 else (i, 2 * i, i % 4) for i in range(100)], ["a", "b", "c"])
freq = df.freqItems(["a", "b", "c"], 0.4)
freq.show()
# 组合的频繁项
freq = df.withColumn('ab', F.struct('a', 'b')).freqItems(['ab'], 0.4)
freq.show()
df.withColumn('ab', array('a', 'b')).freqItems(['ab'], 0.4).show()
```
