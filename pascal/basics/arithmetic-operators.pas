PROGRAM arithmetic_operators;
BEGIN
    WRITELN(10 + 20);               // 30
    WRITELN(20 - 10);               // 10
    WRITELN(10 * 20);               // 200
    WRITELN(20 / 10);               // 2.0...

    // floating point conversion
    WRITELN(10.0 + (10 + 20));      // 40.0...
    WRITELN(20.0 - (10 + 10));      // 0.0...
    WRITELN(10.0 * (10 * 2));       // 200.0...

    // division
    WRITELN(30 / 20);               // 1.5...
    WRITELN(30 div 20);             // 1

    // modulo, remainder
    WRITELN(12 mod 10);             // 2
    WRITELN(10 mod 20);             // 10
END.