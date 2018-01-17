
## [符号语法糖][1]
---

- if
```scala
if(布尔表达式){
   // 如果布尔表达式为 true 则执行该语句块
}else{
   // 如果布尔表达式为 false 则执行该语句块
}
```
---
## 函数
```scala
def functionName ([参数列表]) : [return type] = {
   function body
   return [expr]
}
```
- 匿名函数
```scala
var f = (x:Int) => x + 1
```
- 可变参数
```scala
def addInt(a: Int*): Int = {
  var l = 0
  for (i <- a) {
    l = l + i
  }
  return l
}
```


---
[1]: http://blog.csdn.net/bobozhengsir/article/details/13023023
