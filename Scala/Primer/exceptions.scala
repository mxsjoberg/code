try {
    // do something
}
catch {
    case a: ArithmeticException => println("This is an arithmetic error: " + a)
    case b: Throwable => println("Error: " + b)
}
finally {
    // do something
}