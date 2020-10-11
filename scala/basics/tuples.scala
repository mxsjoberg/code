// NOTE: tuples are immutable
val tuple_one = (1.0, "String", 4)              // (1.0,String,4)
val tuple_two = ("Alpha", "Bravo", (1, 0))      // (Alpha,Bravo,(1,0))

// get value
tuple_one._2                                    // String
tuple_two._3._2                                 // 0

// assign each value in tuple to a variable
val (first, second, third) = ("Alpha", "Beta", "Gamma")
first                                           // Alpha
second                                          // Beta
third                                           // Gamma