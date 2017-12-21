
```python
class SparkML(object):

    def __init__(self, df, _id='id', _label='label'):
        self.df = df
        self.id_label = [_id, _label]

    @classmethod
    def vector_assembler(cls, df, _id='id', _label='label'):
        cls = cls(df, _id=_id, _label=_label)
        '''
        model = SparkML.vector_assembler(df).fit(df)
        model.write().overwrite().save('/user/fbidm/modelresult/ml_pipline_preprocessing.model')
        model.transform(df).select('acct_no', 'label', 'features').saveAsTable('fbidm.yuanjie_train_data', mode='overwrite')
        '''
        strCol = [i[0] for i in cls.df.dtypes if i[1] == 'string' and i[0] not in cls.id_label]
        str2num_ls = [StringIndexer(inputCol=i, outputCol="_" + i, handleInvalid='skip') for i in strCol]
        numCol = [i for i in cls.df.columns + ['_' + i for i in strCol] if i not in cls.id_label + strCol]
        vectorAssembler = VectorAssembler(inputCols=numCol,
                                          outputCol='features')
        stages = str2num_ls + [vectorAssembler]
        return Pipeline(stages=stages)
```
## 实例
```
deploy_date = '20180108'
df = spark.table('fbidm.yuanjie_train_data')
model = SparkML.vector_assembler(df, _id='acct_no').fit(df)
model.write().overwrite().save('/user/fbidm/modelresult/vector_assembler_%s.model' % deploy_date)
model.transform(df).select('acct_no', 'label', 'features').saveAsTable('fbidm.yuanjie_train_data_%s' % deploy_date, mode='overwrite')

```
