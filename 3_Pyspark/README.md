<h1 align = "center">:rocket: PySpark :facepunch:</h1>

---
https://github.com/jadianes/spark-py-notebooks

https://github.com/awantik/pyspark-tutorial

https://github.com/XD-DENG/Spark-practice
---
```python
# Array、Vector互转
arrayToVector = udf(lambda x: Vectors.dense(x), VectorUDT())
vectorToArray = udf(lambda x: [float(i) for i in x], ArrayType(FloatType()))
```
## Tools
- [spark-df-profiling][5]
- [spark-sklearn][6]
- [pyspark-twitter-stream-mining][7]

---
## [常用操作][11]
- [数据重塑][13]
- [返回布尔型][12]

---
## 常用函数
- [基础函数][1]
- [聚合函数][2]
- [窗口函数][3]
- [自定义函数][4]

---
## 常用算法
- [ALS][21]
- [FPGrowth][22]









---
[11]: https://github.com/Jie-Yuan/0_BigData/tree/master/3_Pyspark/1_CommonOperation
[12]: https://github.com/Jie-Yuan/0_BigData/blob/master/3_Pyspark/1_CommonOperation/ReturnBoolean.md
[13]: https://github.com/Jie-Yuan/0_BigData/blob/master/3_Pyspark/1_CommonOperation/DataReshape.md

[21]: http://nbviewer.jupyter.org/github/Jie-Yuan/0_BigData/blob/master/3_Pyspark/2_PysparkML/ALS.ipynb
[22]: https://github.com/Jie-Yuan/0_BigData/blob/master/3_Pyspark/2_PysparkML/FPGrowth.md

[1]: https://github.com/Jie-Yuan/3_PythonLearning/blob/master/5_Spark-Hive_UDFs/CommonFunction.md
[2]: http://blog.csdn.net/skywalker_only/article/details/38823387
[3]: https://github.com/Jie-Yuan/3_PythonLearning/blob/master/5_Spark-Hive_UDFs/WindowFunctions.md
[4]: https://github.com/Jie-Yuan/3_PythonLearning/tree/master/5_Spark-Hive_UDFs
[5]: https://github.com/julioasotodv/spark-df-profiling
[6]: https://github.com/databricks/spark-sklearn
[7]: https://github.com/ambodi/pyspark-twitter-stream-mining

