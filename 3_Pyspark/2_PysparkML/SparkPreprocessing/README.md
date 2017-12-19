```python
class SparkPreprocessing(object):
    def __init__(self, df):
        self.df = df
        self.colName = df.columns
        self.df2array = lambda df: np.array(df.collect())[0]
    def distinct_count(self):
        _array = self.df2array(self.df.select([countDistinct(i).name('_' + i) for i in self.colName]))
        return self.df.select([i for i, j in zip(self.colName, _array) if j != 1])

    def na_prop(self, thresh=0.9):
        _count = self.df.count()
        _array = self.df2array(self.df.select([(1-count(i)/_count).name('_' + i) for i in self.colName]))
        return self.df.select([i for i, j in zip(self.colName, _array) if j < thresh])
```
