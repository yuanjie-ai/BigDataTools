# Hive小结

---

## Hive数据类型
- tinyint: byte
- smallint: short
- int: int
- bigint: long
- float: float
- double: double
- boolean: boolean
- string: varchar
- array: Array(1,2)字段类型相同
- map: Map('a', 1, 'b', 2)键值对
- struct: Struct('a', 1, 1, 0)字段类型可以不同

---

## HSQL
### DDL
- create 
- alter 
- drop
### DML
- load
- insert overwrite
- insert directory
### Functions

---

## Hive调优

```
set mapred.job.tracker=local;
set hive.exec.mode.local.auto=true;
set hive.exec.parallel=true;
set hive.exec.dynamic.partition.mode=nonstrict;
```

### 内存溢出
- map阶段
> 解决：一般存在MapJoin，设置参数set hive.auto.convert.join = false转成reduce端的Common Join
- shuffle阶段
    - 增加reduce数
    ```
    set mapreduce.job.reduces=xxx
    ```
    
    - 调整放在内存里的最大片段所占百分比
    ```
    set mapreduce.reduce.shuffle.memory.limit.percent=0.10
    ```
    
- reduce阶段
    - 增加reduce数（set mapreduce.job.reduces=xxx）。
    - 如果存在数据倾斜，单纯增加reduce个数没有用，参考“Hive优化方法.ppt”进行数据倾斜优化。

### 优化
- 减少样本量
    - 行规约
    - 列规约
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
    
- 小文件合并
    - 输入合并
    ```
    set hive.input.format = org.apache.hadoop.hive.ql.io.combinehiveinputformat;
    set mapred.max.split.size = 536870912;  //512MB
    set mapred.min.split.size = 134217728;  //128MB
    ```
    
    - 输出合并
        - Map-Only任务输出合并
        ```
        set hive.merge.mapfiles=true
        ```
        - MR任务输出合并
        ```
        set hive.merge.mapredfiles=true
        ```
        
- Shuffle: 从map端输出到reduce端输入之间的过程
	- 减小各种IO
	    - 开启中间结果压缩（集群默认开启）
	    ```
	    set mapred.compress.map.output=true
	    ```
	    
	    - 设置中间结果压缩算法
	    ```
	    set mapred.compress.output.compression.codec=com.hadoop.compression.lzo.LzoCodec
	    ```

- JOIN优化
    - MapJoin: 如果一个表非常大、另一个表非常小
    ```默认开启
    set hive.auto.convert.join = true
    ```
    - Common Join优化: 调整reduce个数
    ```
    mapreduce.job.reduces
    ```
    - BucketMapJoin
    ```
    set hive.optimize.bucketmapjoin = true
    ```
    
- 数据倾斜
    - 定位倾斜值
        - join: 关联key集中，处理某值的reduce非常耗时（hive.skewjoin.key特殊值的大小默认100000）
        ```
        set hive.optimize.skewjoin = true
        ```
        
        - group by: 分组key集中，处理某值的reduce非常耗时
        ```
        set hive.groupby.skewindata = true
        ```
        
> 先不按GroupBy字段分发，随机分发做一次聚合
额外启动一轮job，拿前面聚合过的数据按GroupBy字段分发再算结果

---

## 注意事项
- 设置任务名
```
set mapreduce.job.name = JieYuan_job
```
- 分区限制时，涉及日期转换使用to_unix_timestamp方法，而不是unix_timestamp方法
- 公共表表达式
> 语法：
          withClause: cteClause (, cteClause)*
          cteClause: cte_name AS (select statment)
示例：
        with q1 as (select id from src1 where name != 'xiaoming')
        select *
        from src2 t where t.id in (select id from q1);
