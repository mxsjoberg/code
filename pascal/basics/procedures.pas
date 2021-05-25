PROGRAM procedures;

// define procedure (sub-routine)
procedure procedureA;
VAR
    // variables are local
    i: integer = 0;
BEGIN
    WRITELN('i: ', i);
    i += 1;
END;
// end procedure

BEGIN
    procedureA;             // i: 0
    procedureA;             // i: 0
END.