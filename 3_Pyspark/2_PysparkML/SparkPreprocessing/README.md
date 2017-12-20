## 预处理模块
```python
class SparkPreprocessing(object):
    def __init__(self, df, _id='id', _label='label'):
        self.df = df
        self.id_label = [_id, _label]
        self.features_name = [i for i in df.columns if i not in self.id_label]
        __array = np.array(df.groupBy(_label).count().collect())
        self.Y_true = [j for i, j in __array if i == 1][0] + 0.
        self.N_true = [j for i, j in __array if i == 0][0] + 0.
        self.shape = self.Y_true + self.N_true, len(df.columns)
        self.df2array = lambda df: np.array(df.collect())[0]

    @classmethod
    def pipline(cls, df, na_prop_thresh=0.9, iv_thresh=0.1, _id='id', _label='label'):
        cls = cls(df, _id=_id, _label=_label)
        # distinct_count
        _array = cls.df2array(cls.df.select([countDistinct(i).name('_' + i) for i in cls.features_name]))
        col1 = [i for i, j in zip(cls.features_name, _array) if j != 1]
        cls.df = cls.df.select(col1 + cls.id_label).cache()

        # na_prop
        _count = cls.shape[0]
        _array = cls.df2array(cls.df.select([(1 - count(i) / _count).name('_' + i) for i in col1]))
        col2 = [i for i, j in zip(col1, _array) if j < na_prop_thresh]
        cls.df = cls.df.select(col2 + cls.id_label).withColumn('1_label', lit(1) - col(cls.id_label[1])).cache()

        # iv
        _label_name = '%s' % cls.id_label[1]
        _1_label_name = '1_' + _label_name
        cls.df = cls.df.select(col2 + cls.id_label).withColumn(_1_label_name, lit(1) - col(_label_name)).cache()
        y_i = col('sum(%s)' % _label_name)
        n_i = col('sum(%s)' % _1_label_name)
        ls = []
        for i in cls.features_name:
            df_temp = cls.df.groupBy(i).agg({_label_name: 'sum', _1_label_name: 'sum'}) \
                .agg(sum((y_i / cls.Y_true - n_i / cls.N_true) * log((y_i + lit(0.0001)) / (n_i + lit(0.0001)) / (cls.Y_true / cls.N_true))))
            ls.append((cls.df2array(df_temp), i))
        from pprint import pprint
        pprint(sorted(ls, reverse=True))
        return cls.df.select([j for i, j in ls if i > iv_thresh] + cls.id_label)

    @staticmethod
    def fillna(df):
        '''
        :param df:
        :return: 具体项目具体分析
        '''
        numCol1 = [i for i in df.columns if re.search('\d+m|\d*days', i)] + ['score'] # fill 0
        numCol2 = [] # fill -999
        numCol = numCol1 + numCol2
        _numCol = [col(i).astype(FloatType()).name('_' + i) for i in numCol]
        return df.drop(*numCol).select('*', *_numCol).fillna(-999, numCol2).fillna('_NA').fillna(0)

    def distinct_count(self):
        _array = self.df2array(self.df.select([countDistinct(i).name('_' + i) for i in self.features_name]))
        return self.df.select([i for i, j in zip(self.features_name, _array) if j != 1] + self.id_label)

    def na_prop(self, thresh=0.9):
        _count = self.shape[0]
        _array = self.df2array(self.df.select([(1 - count(i) / _count).name('_' + i) for i in self.features_name]))
        return self.df.select([i for i, j in zip(self.features_name, _array) if j < thresh] + self.id_label)

    def iv(self, thresh=0.1):
        _label_name = '%s' % self.id_label[1]
        _1_label_name = '1_' + _label_name
        self.df = self.df.withColumn(_1_label_name, lit(1)-col(_label_name))
        ls=[]
        y_i = col('sum(%s)' % _label_name)
        n_i = col('sum(%s)' % _1_label_name)
        for i in self.features_name:
            df_temp = self.df.groupBy(i).agg({_label_name: 'sum', _1_label_name: 'sum'}) \
            .agg(sum((y_i/self.Y_true - n_i/self.N_true)*log((y_i+lit(0.0001))/(n_i+lit(0.0001))/(self.Y_true/self.N_true))))
            ls.append((self.df2array(df_temp), i))
        from pprint import pprint
        pprint(sorted(ls, reverse=True))
        return self.df.select([j for i, j in ls if i > thresh] + self.id_label)

```

## 简化（效率差一点）
```python
# coding: utf-8
__title__ = 'SparkPreprocessing'
__author__ = 'JieYuan'
__mtime__ = '2017/12/19'


class SparkPreprocessing(object):
    def __init__(self, df, _id='id', _label='label'):
        self.df = df
        self.id_label = [_id, _label]
        self.features_name = [i for i in df.columns if i not in self.id_label]
        __array = np.array(df.groupBy(_label).count().collect())
        self.Y_true = [j for i, j in __array if i == 1][0] + 0.
        self.N_true = [j for i, j in __array if i == 0][0] + 0.
        self.shape = self.Y_true + self.N_true, len(df.columns)
        self.df2array = lambda df: np.array(df.collect())[0]

    @classmethod
    def pipline(cls, df, na_prop_thresh=0.9, iv_thresh=0.1, _id='id', _label='label'):
        _df = cls(df, _id=_id, _label=_label).distinct_count()
        _df = cls(_df, _id=_id, _label=_label).na_prop(thresh=na_prop_thresh)
        _df = cls(_df, _id=_id, _label=_label).iv(thresh=iv_thresh)
        return _df

    @staticmethod
    def fillna(df):
        '''
        :param df:
        :return: 具体项目具体分析
        '''
        numCol1 = [i for i in df.columns if re.search('\d+m|\d*days', i)] + ['score'] # fill 0
        numCol2 = [] # fill -999
        numCol = numCol1 + numCol2
        _numCol = [col(i).astype(FloatType()).name('_' + i) for i in numCol]
        return df.drop(*numCol).select('*', *_numCol).fillna(-999, numCol2).fillna('_NA').fillna(0)

    def distinct_count(self):
        _array = self.df2array(self.df.select([countDistinct(i).name('_' + i) for i in self.features_name]))
        return self.df.select([i for i, j in zip(self.features_name, _array) if j != 1] + self.id_label)

    def na_prop(self, thresh=0.9):
        _count = self.shape[0]
        _array = self.df2array(self.df.select([(1 - count(i) / _count).name('_' + i) for i in self.features_name]))
        return self.df.select([i for i, j in zip(self.features_name, _array) if j < thresh] + self.id_label)

    def iv(self, thresh=0.1):
        _label_name = '%s' % self.id_label[1]
        _1_label_name = '1_' + _label_name
        self.df = self.df.withColumn(_1_label_name, lit(1)-col(_label_name))
        ls=[]
        y_i = col('sum(%s)' % _label_name)
        n_i = col('sum(%s)' % _1_label_name)
        for i in self.features_name:
            df_temp = self.df.groupBy(i).agg({_label_name: 'sum', _1_label_name: 'sum'}) \
            .agg(sum((y_i/self.Y_true - n_i/self.N_true)*log((y_i+lit(0.0001))/(n_i+lit(0.0001))/(self.Y_true/self.N_true))))
            ls.append((self.df2array(df_temp), i))
        from pprint import pprint
        pprint(sorted(ls, reverse=True))
        return self.df.select([j for i, j in ls if i > thresh] + self.id_label)
```
