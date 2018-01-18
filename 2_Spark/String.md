## 字符串
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
- length()
- concat()/+
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
