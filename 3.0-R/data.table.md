# [R：data.table][1]


---
# 数据结构
```
DT = data.table(x=c("b","b","b","a","a"),v=rnorm(5))
```
# 设置键（自动排序）
```
setkey(DT,'x') # 类似pandas索引
DT["A", mult ="first"]
DT["A", mult = "last"]
```
# 切片与df基本一致
- 行切
```
DT['b']
DT[2:4] or DT[2:4,] # 类似pandas
```
- 列切
```
DT[,.(p,q)]
```

# 聚合函数
```
DT[,c('聚合','p'):=.(mean(v),median(v))] # :=增改列（基本都是就地更改）
DT[,.(p,sum=sum(p))] # 列长不一致，循环补齐
```

# 分组聚合
```
DT[,.(sum = sum(v),mean=mean(v)),by=.(x,p)]
DT[,.(sum = sum(v),mean=mean(v)),by=sign(v)] # 按照by分组可以、调用函数分组
DT[, print(.SD), by=x] # .SD包含了各个分组(.SDcols是.SD子集)
DT[,.SD[c(1,.N)],by=x] # 组内第一行或者最后一行
DT[, lapply(.SD, sum), by=x] # 组内每一列的和
```

# 描述性统计
```
DT[,.N,by=x] # 使用函数.N来得到每个类别的总观测数
DT[.N] # 最后一行
DT[,.N] # 行数
```

# 高级操作
```
DT[, .(newcol = sum(p)),by=x][newcol > 0.1] # 分组聚合筛选
DT[, .(newcol = sum(p)),by=x][newcol > 0.1][order(-newcol)]
```

# 多个表达式(行为操作)可以包裹在花括号中
```
DT[,{print(p)
  plot(p) 
  NULL}]
```

  [1]: http://www.cnblogs.com/nxld/p/6059570.html
