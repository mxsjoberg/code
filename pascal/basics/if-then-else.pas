PROGRAM if_then_else;
VAR
    a: real = 1.0;
    b: real = 5.0;
BEGIN
    // one instruction
    if a = 1.0 then WRITELN('a is equal to 1.0')        // a is equal to 1.0
    else WRITELN('a is not equal to 1.0');

    // more than one instruction (or nested)
    if a = 1.0 then
        BEGIN
            if b = 5.0 then
                BEGIN
                    WRITELN('a is equal to 1.0');       // a is equal to 1.0
                    WRITELN('b is equal to 5.0');       // b is equal to 5.0
                END
            else
                WRITELN('b is not equal to 5.0');
            // end if
        END
    else
        WRITELN('a is not equal to 1.0');
    // end if
END.