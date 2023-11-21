// macro to generate getter and setter for struct
macro_rules! generate_getter_setter {
    ($struct_name:ident, { $($field_name:ident: $field_type:ty),* }) => {
        impl $struct_name {
            $(
                fn $field_name(&self) -> $field_type {
                    self.$field_name // return
                }

                // not valid rust?
                fn set_$field_name(&mut self, value: $field_type) {
                    self.$field_name = value; // assign
                }
            )*
        }
    };
}

struct Person {
    Name: String,
    Age: u32,
}

generate_getter_setter!(Person, { Name: String, Age: u32 });

fn main() {
    let mut person = Person {
        Name: String::from("Alice"),
        Age: 42,
    };

    println!("Name: {}", person.Name());
    person.set_name(String::from("Bob"));
    println!("Name: {}", person.Name());
}