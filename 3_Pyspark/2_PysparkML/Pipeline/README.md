```python
def ml_pipline(df, _id='id', _label='label'):
    id_label = [_id, _label]
    strCol = [i[0] for i in df.dtypes if i[1] == 'string' and i[0] not in id_label]
    str2num_ls = [StringIndexer(inputCol=i, outputCol="_" + i, handleInvalid='skip') for i in strCol]
    vectorAssembler = VectorAssembler(inputCols=[i for i in df.columns if i not in id_label + strCol],
                                      outputCol='features')
    stages = str2num_ls + [vectorAssembler]
    return Pipeline(stages=stages)
```
