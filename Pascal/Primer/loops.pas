// 2020-02
program Loops;

var
    x: integer;
    i, j: integer;
    // for readln input
    input: string;
begin
    for i := 1 to 5 do write(i, ' ');
    // 1 2 3 4 5

    // nested
    for i := 0 to 1 do
        for j := 0 to 2 do
            write('(', i, ',', j, ') ');
        // end for
    // end for
    
    // (0,0) (0,1) (0,2) (1,0) (1,1) (1,2)

    // iterate down
    for i := 5 DownTo 0 do writeln(i);
    // 5
    // 4
    // 3
    // 2
    // 1
    // 0

    // while
    x := 0;
    while x < 5 do x += 1;
    writeln(x);
    // 5

    // repeat-until
    i := 0;
    repeat
        begin
            write(i, ' ');
            i += 1;
        end
    until i >= 5;
    // 0 1 2 3 4 

    // repeat until input is equal to value
    repeat readln(input) until input = 'exit';
    // > hello pascal
    // > ...
    // exit
    // ...Program finished with exit code 0
end.