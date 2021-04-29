PROGRAM sets;
TYPE
    // sets are collections of same type
    days = set of (Mon, Tue, Wed, Thu, Fri, Sat, Sun);
    letters = set of char;
    alphabet = set of 'A' .. 'Z';
VAR
    // declare sets
    A: alphabet;
    B: alphabet;
    C: alphabet;

    // declare iterator variables
    i: char;
BEGIN
    A := ['A', 'B', 'C', 'D'];
    for i in A do WRITE(i, ' '); WRITELN();             // A B C D

    B := ['C', 'D', 'E', 'F'];
    for i in B do WRITE(i, ' '); WRITELN();             // C D E F

    // union
    for i in (A + B) do WRITE(i, ' '); WRITELN();       // A B C D E F 

    // intersection
    for i in (A * B) do WRITE(i, ' '); WRITELN();       // C D 

    // difference
    for i in (A - B) do WRITE(i, ' '); WRITELN();       // A B

    // symmetric difference
    for i in (A >< B) do WRITE(i, ' '); WRITELN();      // A B E F 

    // subset
    C := ['A', 'B', 'C'];
    if (C <= A) then WRITELN(true);                     // TRUE

    // include
    INCLUDE(A, 'E');
    for i in A do WRITE(i, ' '); WRITELN();             // A B C D E

    // exclude
    EXCLUDE(A, 'E');
    for i in A do WRITE(i, ' '); WRITELN();             // A B C D

    // in
    if 'A' in A then WRITELN(true);                     // TRUE
END.