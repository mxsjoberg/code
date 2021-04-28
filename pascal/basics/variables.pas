PROGRAM variables;
TYPE
    // define enumerated type
    position = (Left, Right, Up, Down);
    // define range
    range = 1 .. 20;
VAR
    // declare and initialise variables
    x: integer = 6;
    y: string = 'String';
    z: real = 1.05;
    c: char = 'C';

    // declare enumerated variable
    pos: position;
    
    // declare range variable
    r: range;
BEGIN
    WRITELN(x);                 // 6
    WRITELN(y);                 // String
    WRITELN(z);                 // 1.05...
    WRITELN(c);                 // C
    
    // enumerated
    pos := Right;
    WRITELN(pos);               // Right

    // valid range
    r := 12;
    WRITELN(r);                 // 12

    // invalid range
    r := 25;
    WRITELN(r);                 // 25 (Warning: range check error while evaluating constants (25 must be between 1 and 20))
END.
