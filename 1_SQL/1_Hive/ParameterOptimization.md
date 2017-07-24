# 查询优化设置
```
//job name
set mapreduce.job.name = JieYuan_job;
set hive.exec.mode.local.auto=true; //当一个job满足如下条件会使用本地模式
set hive.exec.parallel=true; //开启并行模式
set hive.exec.parallel.thread.number=16; //最大64
set hive.merge.mapfiles=true; //map任务输出合并
set hive.merge.mapredfiles=true; //mr任务输出合并
set mapred.compress.map.output=true; //减少IO开启中间结果压缩
set mapred.compress.output.compression.codec=com.hadoop.compression.lzo.LzoCodec; //设置压缩算法
//join
set hive.auto.convert.join = true;
set mapred.reduce.tasks = -1; //代表自动根据作业的情况来设置reduce的值
set hive.optimize.bucketmapjoin = true;
//数据倾斜
set hive.optimize.skewjoin = true;
set hive.groupby.skewindata = true;
```