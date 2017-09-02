# :rocket: [RedisLearning][1] :facepunch:
---
## [Redis常用操作][2]
```
import redis
pool = redis.ConnectionPool(host='10.37.107.218', port=6379, db=0)
r = redis.Redis(connection_pool = pool)
```
## 插
```
r.set('yuanjie',{'aaaaa'})
```
## 查
```
r.get('yuanjie')

b"{'aaaaa'}"
```
## 删
```
r.delete('yuanjie')
```











---
[1]: http://www.runoob.com/redis/redis-tutorial.html
[2]: http://www.cnblogs.com/melonjiang/p/5342505.html
