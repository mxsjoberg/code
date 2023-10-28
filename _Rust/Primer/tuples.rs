fn main() {
    // tuples are fixed-size (underscore to indicate unused variable)
    let _tuple_one = (1.0, "hello rust", 4);

    // type annotation
    let tuple_one: (f64, &'static str, i32) = (1.0, "hello rust", 4);

    println!("{:?}", tuple_one);
    // (1.0, "hello rust", 4)

    // nested tuples
    let tuple_two = ("alpha", "beta", (1, 0));

    println!("{:?}", tuple_two);                    // ("alpha", "beta", (1, 0))
    println!("{:?}", tuple_two.2);                  // (1, 0)
    println!("{:?}", (tuple_two.2).0);              // 1

    // destructuring
    let (x, y, z) = tuple_one;

    println!("{:?} {:?} {:?}", x, y, z);
    // 1.0 "hello rust" 4
}