// 2020-02
program Sets;

type
    // sets are collections of same type
    days_of_week = set of (Mon, Tue, Wed, Thu, Fri, Sat, Sun);
    letters = set of char;
    alphabet = set of 'A' .. 'Z';
var
    // declare sets
    A: alphabet;
    B: alphabet;
    C: alphabet;

    days: days_of_week;

    // declare iterator variables
    i: char;
begin
    A := ['A', 'B', 'C', 'D'];
    for i in A do write(i, ' '); writeln();
    // A B C D

    B := ['C', 'D', 'E', 'F'];
    for i in B do write(i, ' '); writeln();
    // C D E F

    // union
    for i in (A + B) do write(i, ' '); writeln();
    // A B C D E F 

    // intersection
    for i in (A * B) do write(i, ' '); writeln();
    // C D 

    // difference
    for i in (A - B) do write(i, ' '); writeln();
    // A B

    // symmetric difference
    for i in (A >< B) do write(i, ' '); writeln();
    // A B E F 

    // subset
    C := ['A', 'B', 'C'];
    if (C <= A) then writeln(true);
    // TRUE

    // include
    include(A, 'E');
    for i in A do write(i, ' '); writeln();
    // A B C D E

    // exclude
    exclude(A, 'E');
    for i in A do write(i, ' '); writeln();
    // A B C D

    // in
    if 'A' in A then writeln(true);
    // TRUE

    days := [Mon, Wed, Fri];
    if Wed in days then writeln(true);
    // TRUE
end.