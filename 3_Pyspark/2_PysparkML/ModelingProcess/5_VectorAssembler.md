<h1 align = "center">:rocket: 特征向量化 :facepunch:</h1>

---
```python

from pyspark.ml.feature import VectorAssembler

class SparkML(object):
    def __init__(self, df, _id, _label):
        self.df = df
        self.id_label = [_id, _label]

    @classmethod
    def vector_assembler_hash_coding(cls, df, _id='id', _label='label', strColName=None):
        cls = cls(df, _id=_id, _label=_label)
        strColName = [i for i, j in cls.df.dtypes if j == 'string' and i not in cls.id_label]
        for i in strColName:
            cls.df = cls.df.withColumn(i, hash(i))

        numCol = [i for i in cls.df.columns if i not in cls.id_label]
        vectorAssembler = VectorAssembler(inputCols=numCol, outputCol='features')
        if _label:
            df = vectorAssembler.transform(df).select(_id, _label, 'features')
        else:
            df = vectorAssembler.transform(df).select(_id, 'features')
        return df

    def cv(self):
        pass

```
---

## 实例
```
deploy_date = '20180108'
df = spark.table('fbidm.yuanjie_train_data')
model = SparkML.vector_assembler(df, _id='acct_no', _label='label', path='/user/fbidm/modelresult/vector_assembler_%s.model'  %deploy_date)
df = model.transform(df).select('acct_no', 'label', 'features')
df.write.saveAsTable('fbidm.yuanjie_train_data_%s' % deploy_date, mode='overwrite')
```
