use std::thread;
use std::sync::{ Arc, Mutex };
use std::sync::mpsc; // multiple producer, single consumer
// use std::ops::Add; // + operator as trait

// custom trait to extend behaviour of Add operator
trait BetterAdd<RHS=Self> {
    type Output;
    fn better_add(self, rhs: RHS) -> Self::Output;
}

impl BetterAdd<i32> for f32 {
    type Output = f32;
    fn better_add(self, rhs: i32) -> f32 {
        self + rhs as f32
    }
}

fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // channel for send an receive
    let (tx, rx) = mpsc::channel();

    // mutexed accumulator for sum
    let sum = Arc::new(Mutex::new(0.0));

    // spawn threads
    for chunk in numbers.chunks(3) {
        let tx = tx.clone();
        let sum = Arc::clone(&sum);

        // not working?
        thread::spawn(move || {
            let partial_sum: f32 = chunk.iter().map(|&x| x).fold(0.0, |acc, x| acc.better_add(x));
            let mut sum = sum.lock().unwrap();
            *sum = sum.better_add(partial_sum);
            tx.send(()).unwrap();
        });
    }

    // wait for threads to finish
    for _ in 0..numbers.len() / 3 {
        rx.recv().unwrap();
    }

    // print result
    println!("Sum is {}", *sum.lock().unwrap());
}
