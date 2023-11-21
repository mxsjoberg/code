// 2020-02
program Functions;

// define function
function power(base: integer; x: integer) : integer;
var
    // local variables
    result: integer = 1;
    i: integer = 0;
begin
    while i < x do
    begin
        result := result * base;
        i := i + 1;
    end;
    power := result;
end;

begin
    writeln(power(2, 8));
    // 256
end.