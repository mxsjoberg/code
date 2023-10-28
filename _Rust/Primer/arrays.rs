fn main() {
    // arrays are fixed-size
    let numbers = [200.0, -2.2, 1.0, 0.0];
    let names = ["Adam", "John", "Michael", "Susan"];

    println!("{:?}", numbers);                              // [200.0, -2.2, 1.0, 0.0]
    println!("{:?}", names);                                // ["Adam", "John", "Michael", "Susan"]

    // length
    println!("{:?}", numbers.len());
    // 4

    // indexing
    println!("{:?}", numbers[0]);                           // 200.0
    println!("{:?}", names[2]);                             // "Michael"
    println!("{:?}", names[names.len() - 1]);               // "Susan"

    // slice (reference is required)
    println!("{:?}", &numbers[0..2]);
    // [200.0, -2.2]

    // arrays are immutable by default
    // numbers[0] = 100.0;
    // cannot assign to `numbers[_]`, as `numbers` is not declared as mutable

    // assignment
    let mut numbers = [200.0, -2.2, 1.0, 0.0];

    numbers[0] = 50.0;
    println!("{:?}", numbers[0]);
    // 50.0

    // n-dimensional arrays
    let matrix = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]];

    println!("{:?}", matrix[1][2]);
    // 7
}