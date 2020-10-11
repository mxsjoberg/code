def function(): Boolean = {
    // do something
    return true
}

// example
def add(a:Int, b:Int): Int = {
    return a + b
}

add(2, 3)
// 5

// default arguments
def add(a:Int, b:Int = 3): Int = {
    return a + b
}

add(2)
// 5

// multiple return values
def add(a:Int, b:Int): (Int, Int, Int) = {
    var result = a + b

    return (a, b, result)
}

val (a, b, result) = add(2, 3)
// (2,3,5)

// NOTE: documentation (scaladoc style)

/** This is documentation for defined function.
 *
 *  @param arg is an argument
 */
def function(arg:Any) = {    
    // do something
}