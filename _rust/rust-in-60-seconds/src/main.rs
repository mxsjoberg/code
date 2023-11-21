/*
    cargo new path/to/folder
*/

use std::io;
use std::collections::HashMap;

// structs
struct Person {
    name: String,
    age: u32, // unsigned 32 bit integer
}

// enums
#[allow(dead_code)] // suppress warnings for unused variants
enum Color {
    Red,
    Green, 
    Blue,
}

// traits and implementations
impl Person {
    fn greet(&self) {
        println!("Hello, my name is {} and my age is {}.", self.name, self.age);
    }
}

fn main() {
    println!("Rust in 60 seconds!");

    // variables and mutability
    let mut counter = 0;
    counter += 1;

    // control flow
    if counter > 0 {
        println!("Counter is greater than 0.");
    } else {
        println!("Counter is less than 0.");
    }

    // loops
    for i in 0..5 {
        println!("Iteration {}", i);
    }

    // pattern matching
    let number = 42;
    match number {
        0 => println!("It's zero."),
        1..=100 => println!("It's between 1 and 100."),
        _ => println!("It's something else."),
    }

    // option and result
    let result: Result<i32, String> = Ok(42);
    match result {
        Ok(value) => println!("Result is {}", value),
        Err(err) => println!("Error {}", err),
    }

    // structs and methods
    let person = Person {
        name: String::from("Alice"),
        age: 42,
    };
    person.greet();

    // vectors
    let mut numbers = vec![1, 2, 3];
    numbers.push(4);

    // hashmap
    let mut scores = HashMap::new();
    scores.insert(String::from("Alice"), 100);
    scores.insert(String::from("Bob"), 200);

    // enums
    let color = Color::Red;
    match color {
        Color::Red => println!("It's red."),
        Color::Green => println!("It's green."),
        Color::Blue => println!("It's blue."),
    }

    // file io
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line.");
    println!("You typed: {}", input.trim());
    // You typed: hello rust

    // ownership
    let value = String::from("ABCDEF");
    take_ownership(value); // .clone() to avoid moving value
    // println!("Value: {}", value); // compile-time error

    // borrowing
    let message = String::from("This is my message.");
    let len = calculate_length(&message); // &message is a reference to message
    println!("Length of message is {}.", len);
    // Length of message is 19.
}

fn take_ownership(value: String) {
    println!("Value: {}", value);
    // nothing is returned at the end of this function
}

fn calculate_length(s: &String) -> usize {
    s.len() // s is returned at the end of this function
}
