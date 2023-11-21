PROGRAM repeat_until_loop;
VAR
    a: integer = 5;
    n: integer = 0;

    // string input
    input: string;
BEGIN
    repeat
        BEGIN
            WRITELN(n);
            n += 1;
        END
    until n >= a;
    // 0
    // 1
    // 2
    // 3
    // 4

    // repeat until input is equal to value
    repeat READLN(input) until input = 'exit';
    // > hello
    // > pascal
    // > exit
END.