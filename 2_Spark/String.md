## [字符串][1]
```scala
object Test {
   def main(args: Array[String]) {
      val buf = new StringBuilder; // String对象是不可变的, StringBuilder可变
      buf += 'a'
      buf ++= "bcdef"
      println( "buf is : " + buf.toString );
   }
}
```
- 字符串格式化
```scala
object Test {
  def main(args: Array[String]) {
    var floatVar = 12.456
    var intVar = 2000
    var stringVar = "菜鸟教程!"
    var fs = printf("浮点型变量: %f " +
      "整型变量: %d " +
      "字符串: %s ",
      floatVar, intVar, stringVar)
    println(fs)
  }
}
```
- length()
- concat()/+
- trim(): 删除指定字符串的首尾空白符



---
[1]: http://www.yiibai.com/scala/scala_strings.html
