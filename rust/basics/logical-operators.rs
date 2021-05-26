#[allow(non_snake_case)]

fn main() {
    let T: bool = true;
    let F: bool = false;

    // and, or
    println!("{:?}", T && F);           // false
    println!("{:?}", T && (T || F));    // true

    // not
    println!("{:?}", !T);               // false
    println!("{:?}", !(!T));            // true

    // relational
    println!("{:?}", 1 == 2);           // false
    println!("{:?}", 1 != 2);           // true
    println!("{:?}", 1 > 2);            // false
    println!("{:?}", 1 < 2);            // true
    println!("{:?}", 1 >= 2);           // false
    println!("{:?}", 1 <= 2);           // true
}