PROGRAM logical_operators;
VAR
    T: boolean = true;
    F: boolean = false;
BEGIN
    // and, or
    WRITELN(T and F);           // FALSE
    WRITELN(T and (T or F));    // TRUE

    // not
    WRITELN(not T);             // FALSE
    WRITELN(not (not T));       // TRUE

    // relational
    WRITELN(1 = 2);             // FALSE
    WRITELN(1 <> 2);            // TRUE
    WRITELN(1 > 2);             // FALSE
    WRITELN(1 < 2);             // TRUE
    WRITELN(1 >= 2);            // FALSE
    WRITELN(1 <= 2);            // TRUE
END.