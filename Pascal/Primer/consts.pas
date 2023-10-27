// 2020-02
program Consts;

const
    A = 100;
    B = 200;
begin
    writeln(A * B);
    // 20000

    // consts are immutable
    // A := 42;
    // Error: Variable identifier expected
end.