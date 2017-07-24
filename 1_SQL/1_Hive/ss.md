- 如何合理的设置map、reduce个数
    - Map
        - HDFS块大小（dfs.block.size: 128M）
        - 文件的大小
        - 文件的个数
        - splitsize的大小

        ```
splitSize = Math.max(minSize, Math.min(maxSize, blockSize))
        ```

    - Reduce
    ```
    reducers = Math.min(maxReducers, totalInputFileSize/bytesPerReducer)
    maxReducers = hive.exec.reducers.max默认999
    bytesPerReducer = hive.exec.reducers.bytes.per.reducer 
    mapreduce.job.reduces
    ```
