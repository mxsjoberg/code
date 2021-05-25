PROGRAM case_else;
VAR
    a: integer = 1;
BEGIN
    case a of
        1: WRITELN('One');
        2: WRITELN('Two');
        3: WRITELN('Three');
    else
        WRITELN('None');
    end;
    // One
END.