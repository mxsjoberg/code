// NOTE: val is immutable
val x: Int = 6
val y: String = "String"
val z: Double = 1.05

x, y, z                                 // (6,String,1.05)
x.getClass.getSimpleName                // int
y.getClass.getSimpleName                // String
z.getClass.getSimpleName                // double

// NOTE: var is mutable
var a = x                               // 6
a = a + 2                               // 8

// multiple assignment
val (x, y, z) = (6, "String", 1.05)     // (6,String,1.05)

// list assignment
val List(d, t, v) = List(230, 45, 12)   // (230,45,12)

// string assignment
val string: String = "100B"
val Array(a, b, c, d) = string.toArray  // (1,0,0,B)