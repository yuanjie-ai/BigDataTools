# :rocket: [HBaseLearning][1] :facepunch:
---
## [Happybase]
```
.\site-packages\thriftpy\parser\parser.py line 488  
-  if url_scheme == '':
+  if len(url_scheme) <= 1:
```
---
## 建表
```
import happybase
connection =  happybase.Connection('namenode1-sit.cnsuning.com', 9090)
families = {'f': dict()}
connection.create_table('ns_firs:yuanjie_table', families=families)
tab = connection.table('ns_firs:yuanjie_table')
tab.families()

{b'f': {'block_cache_enabled': False,
  'bloom_filter_nb_hashes': 0,
  'bloom_filter_type': b'NONE',
  'bloom_filter_vector_size': 0,
  'compression': b'NONE',
  'in_memory': False,
  'max_versions': 3,
  'name': b'f:',
  'time_to_live': 2147483647}}
```
## 插表
```
tab.put('jieyuan', {'f:c1': 'a'}) # 列簇可以对应多列
tab.put('yuanjie', {'f:c1': 'a', 'f:c2': 'b'})
```
## 查表
```
tab.row('yuanjie')
tab.rows(['jieyuan', 'yuanjie'])
list(tab.scan())

{b'f:c1': b'a'}
[(b'jieyuan', {b'f:c1': b'a'}), (b'yuanjie', {b'f:c1': b'a', b'f:c2': b'b'})]
[(b'jieyuan', {b'f:c1': b'a'}), (b'yuanjie', {b'f:c1': b'a', b'f:c2': b'b'})]
```
## 删表
```
connection.delete_table('ns_firs:yuanjie_table', disable = True)
```


---
## 数据定义语言
- connection.compact_table # 压缩指定的表
- connection.create_table
- connection.delete_table
- connection.disable_table # 禁用指定的表
- connection.enable_table  # 启用指定的表
- connection.open
- connection.table
- connection.tables
- connection.transport
---
## 数据操纵语言
- tab.families # 相当于表结构(列簇)
- tab.regions  # 此表区域
- tab.cells    # 从表中检索单个单元格的多个版本
- tab.put      # 把指定列在指定的行中单元格的值在一个特定的表
- tab.delete
- tab.row
- tab.rows
- tab.scan
---

[1]: http://www.yiibai.com/hbase/
