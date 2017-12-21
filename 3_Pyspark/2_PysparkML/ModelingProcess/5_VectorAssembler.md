<h1 align = "center">:rocket: 特征向量化 :facepunch:</h1>

---
```python
class SparkML(object):
    def __init__(self, df, _id, _label, path):
        self.df = df
        self.id_label = [_id, _label]
        self.path = path

    @classmethod
    def vector_assembler(cls, df, _id='id', _label='label', path='/user/fbidm/modelresult/vector_assembler.model'):
        cls = cls(df, _id=_id, _label=_label)
        '''
        model.transform(df).select('acct_no', 'label', 'features').saveAsTable('fbidm.yuanjie_test', mode='overwrite')
        '''
        strCol = [i[0] for i in cls.df.dtypes if i[1] == 'string' and i[0] not in cls.id_label]
        str2num_ls = [StringIndexer(inputCol=i, outputCol="_" + i, handleInvalid='skip') for i in strCol]
        numCol = [i for i in cls.df.columns + ['_' + i for i in strCol] if i not in cls.id_label + strCol]
        vectorAssembler = VectorAssembler(inputCols=numCol,
                                          outputCol='features')
        stages = str2num_ls + [vectorAssembler]
        model = Pipeline(stages=stages).fit(df.cache())
        model.write().overwrite().save(cls.path)
        print("Save Model Path: " + cls.path)
        # model = PipelineModel.load('test.model')
        return model

    def cv(self):
        pass

```
---

## 实例
```
deploy_date = '20180108'
df = spark.table('fbidm.yuanjie_train_data')
model = SparkML.vector_assembler(df, _id='id', _label='label', path='/user/fbidm/modelresult/vector_assembler.model')
model.transform(df).select('acct_no', 'label', 'features') \
.write.saveAsTable('fbidm.yuanjie_train_data_%s' % deploy_date, mode='overwrite')
```
