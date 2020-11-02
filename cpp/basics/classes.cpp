// OUTSIDE SCOPE: create a class
class MyClass {
    private:
        // private attributes
        int hidden;
    public:
        // public attributes
        int number;
        string str;
        // methods
        string get_name() {
            return "MyClass";
        }
        int get_hidden() {
            return hidden;
        }
        void set_hidden(int i) {
            hidden = i;
        }
        // constructor: called when instance of class is created
        MyClass() {
            cout << "Created class: " << get_name() << endl;
        }
};

// INSIDE SCOPE: create instance of class
MyClass obj;
// Created class: MyClass

// access public attributes
obj.number = 10;                    // 10
obj.str = "String";                 // String

// access private attributes
obj.set_hidden(5);
obj.get_hidden();
// 5

// OUTSIDE SCOPE: create a subclass
class MySubClass: public MyClass {
    public:
        bool value;
        // override
        string get_name() {
            return "MySubClass";
        }
        // constructor: called when instance of class is created
        MySubClass() {
            cout << "Created class: " << get_name() << endl;
        }
};

// INSIDE SCOPE: create instance of class
MySubClass obj_sub;
// Created class: MyClass
// Created class: MySubClass

obj_sub.value = true;
// 1