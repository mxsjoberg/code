fn main() {
    println!("{}", 10 + 20);                        // 30
    println!("{}", 20 - 10);                        // 10
    println!("{}", 10 * 20);                        // 200
    println!("{}", 20 / 10);                        // 2

    // power (type is required)
    println!("{}", i32::pow(10, 2));
    // 100

    // floating-point conversion
    println!("{}", 10.0 + ((10 + 20) as f64));
    // 40

    // common division error
    println!("{}", 30 / 20);                        // 1 (quotient)
    println!("{}", 30.0 / 20.0);                    // 1.5

    // modulo, remainder
    println!("{}", 12.5 % 10.0);                    // 2.5
    println!("{}", 10.0 % 20.0);                    // 10

    // built-ins (type is required)
    println!("{}", i32::abs(-20));                  // 20
    println!("{}", i32::min(2, 5));                 // 2
    println!("{}", i32::max(2, 5));                 // 5

    // rounding values (type is required)
    println!("{}", f64::round(2.945));              // 3
    println!("{}", f64::trunc(2.945));              // 2
    println!("{}", f64::floor(2.945));              // 2
}