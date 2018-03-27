```python
import dask
import dask.dataframe as dd
import pandas as pd
from dask.multiprocessing import get 
from multiprocessing import cpu_count 
nCores = cpu_count() 

# pandas
my_df.apply(lambda x: nearest_street(x.lat,x.lon),axis=1) 

# dask
dd.from_pandas(my_df,npartitions=nCores).\ 
   map_partitions(\ 
     lambda df : df.apply(\ 
         lambda x : nearest_street(x.lat,x.lon), axis=1)).\ 
     compute(get=get) 
     
     
# ddf.map_overlap
# ddf.map_partitions


# ddf.persist
# ddf.reduction

# ddf.repartition ########### 改变线程
# ddf.npartitions ########### 线程数
```
