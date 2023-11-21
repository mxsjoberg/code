// 2020-02
program Variables;

type
    // define enumerated type
    position = (Left, Right, Up, Down);
    // define range
    range = 1 .. 20;
var
    number: integer = 42;
    text: string = 'this is some text';
    float: real = 12.5;
    ch: char = 'A';

    // declare enumerated variable
    pos: position;
    
    // declare range variable
    rng: range;
begin
    writeln(number);
    // 42
    writeln(text);
    // this is some text
    writeln(float);
    // 12.5...
    writeln(ch);
    // A
    
    // enumerated
    pos := Right;
    writeln(pos);
    // Right

    // valid range
    rng := 12;
    writeln(rng);
    // 12

    // invalid range
    rng := 25;
    writeln(rng);
    // Warning: range check error while evaluating
    // constants (25 must be between 1 and 20)
end.
