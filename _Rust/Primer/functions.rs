//! Documentation (support markdown)
//!
//! # Function
//!
//! ```
//! assert_eq!(42, function(42))
//! fn function(arg: i32) -> i32 {
//!     // do something
//!     return arg;
//! }
//! ``
fn function(arg: i32) -> i32 {
    // do something
    return arg;
}

// example (return statement is optional)
fn power(x: i32, n: i32) -> i32 {
    let mut result: i32 = 1;
    // multiply x with itself n times
    for _i in 1..n {
        if result == 1 {
            result = x * x;
        } else {
            result *= x;
        }
    }
    result
}

fn main() {
    println!("{:?}", function(42));             // 42
    println!("{:?}", power(2, 3));              // 8
}