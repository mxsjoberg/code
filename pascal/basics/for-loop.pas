PROGRAM for_loop;
VAR
    i, j: integer;
BEGIN
    for i := 1 to 5 do WRITELN(i);
    // 1
    // 2
    // 3
    // 4
    // 5

    // nested
    for i := 0 to 2 do
        for j := 0 to 2 do
            WRITELN('(i, j): (', i, ', ', j, ')');
        // end for
    // end for

    // (i, j): (0, 0)
    // (i, j): (0, 1)
    // (i, j): (0, 2)
    // (i, j): (1, 0)
    // (i, j): (1, 1)
    // (i, j): (1, 2)
    // (i, j): (2, 0)
    // (i, j): (2, 1)
    // (i, j): (2, 2)

    // iterate down
    for i := 5 DownTo 0 do WRITELN(i);
    // 5
    // 4
    // 3
    // 2
    // 1
    // 0
END.