#[allow(unused_assignments)]
#[allow(unused_variables)]

fn main() {
    // type annotations are optional
    let x = 6;
    let y: f64 = 1.05;
    let z: &'static str = "hello rust";
    let c: char = 'A';

    println!("{:?} {:?} {:?} {:?}", x, y, z, c);
    // 6 1.05 "hello rust" 'A'

    // pattern assignment
    let (d, t, v) = (230, 45, 12);
    println!("{:?} {:?} {:?}", d, t, v);
    // 230 45 12

    // variables are immutable by default
    // x = 10;
    // cannot assign twice to immutable variable `x`

    // mutable variables
    let mut x = 6;
    x = 10;

    println!("{:?}", x);
    // 10

    // make mutable variable immutable
    let x = x;
    // x = 10;
    // cannot assign twice to immutable variable `x`

    // variable size type
    let u: usize = 10;

    println!("{:?}", u);
    // 10
}