// NOTE: sets are immutable
val set_numbers: Set[Int] = Set(1, 3, 5, 7, 9)      // Set(5, 1, 9, 7, 3)

set_numbers.contains(3)                             // true
set_numbers.contains(2)                             // false

// mutable set
val set_mutable_one = scala.collection.mutable.Set(1, 3, 5)
val set_mutable_two = scala.collection.mutable.Set(5, 7, 9)

set_mutable_two += 11                               // Set(9, 5, 7, 11)
set_mutable_two -= 11                               // Set(9, 5, 7)

// set operations
val A = set_mutable_one.clone
val B = set_mutable_two.clone

A | B                                               // Set(9, 1, 5, 3, 7)
A & B                                               // Set(5)
A &~ B                                              // Set(1, 3)

A union B                                           // Set(9, 1, 5, 3, 7)
A intersect B                                       // Set(5)
A diff B                                            // Set(1, 3)

A subsetOf B                                        // false