PROGRAM constants;
CONST
    LENGTH = 10;
    HEIGHT = 15;
BEGIN
    WRITELN(LENGTH * HEIGHT);
    // 150

    // constants are immutable
    LENGTH := 5;
    // Error: Variable identifier expected
END.