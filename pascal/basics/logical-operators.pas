PROGRAM logicaloperators;
VAR
    T: boolean = true;
    F: boolean = false;
BEGIN
    WRITELN(T);                 // TRUE
    WRITELN(F);                 // FALSE

    // operators
    WRITELN(T or F);            // TRUE
    WRITELN(T and (T and F));   // FALSE
    WRITELN(not T);             // FALSE
    WRITELN(not (not T));       // TRUE

    // equality
    WRITELN(1 = 2);             // FALSE
    WRITELN(1 <> 2);            // TRUE
END.