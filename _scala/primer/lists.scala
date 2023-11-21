// lists are immutable
val list_one: List[String] = List("Alpha", "Beta")          // List(Alpha, Beta)
val list_two: List[Any] = List(200, -2, List(1.0, 0.0))     // List(200, -2, List(1.0, 0.0))
val list_range: List[Int] = List.range(1, 10)               // List(1, 2, 3, 4, 5, 6, 7, 8, 9)

// concatenate lists
val list_all = list_one ++ list_two                         // List(Alpha, Beta, 200, -2, List(1.0, 0.0))

// append to list by creating a new list
val list_one_new = "Gamma"  :: list_one                     // List(Gamma, Alpha, Beta)

// built-ins
list_one_new.length                                         // 3
list_one_new.sorted                                         // List(Alpha, Beta, Gamma)
list_two.head                                               // 200
list_two.last                                               // List(1.0, 0.0)
list_range.filter(_ > 5)                                    // List(6, 7, 8, 9)

// create list from string
val list_char: List[Char] = ("100B").toList                 // List(1, 0, 0, B)