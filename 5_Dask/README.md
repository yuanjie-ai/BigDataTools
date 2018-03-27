```python
# pandas
my_df.apply(lambda x: nearest_street(x.lat,x.lon),axis=1) 

# dask
dd.from_pandas(my_df,npartitions=nCores).\ 
   map_partitions(\ 
     lambda df : df.apply(\ 
         lambda x : nearest_street(x.lat,x.lon), axis=1)).\ 
     compute(get=get) 
```
