# :rocket: DataReshape :facepunch:
---
```
df = spark.createDataFrame([('G', 'X', 1), 
                            ('G', 'Y', 2), 
                            ('G', 'X', 3), 
                            ('H', 'Y', 4), 
                            ('H', 'Z', 5)], list('ABC'))
df.show()
```
---
## 长变宽
```
df.groupBy('A').pivot('B').max('C').show()

+---+----+---+----+
|  A|   X|  Y|   Z|
+---+----+---+----+
|  G|   3|  2|null|
|  H|null|  4|   5|
+---+----+---+----+
```
---
## 宽边长
```
df = df.groupBy('A').pivot('B').max('C')
df.selectExpr("A", "stack(3, 'X', X, 'Y', Y, 'Z', Z) as (B, C)").where("C is not null").show()

+---+---+---+
|  A|  B|  C|
+---+---+---+
|  G|  X|  3|
|  G|  Y|  2|
|  H|  Y|  4|
|  H|  Z|  5|
+---+---+---+
```
