// 2020-02
program Procedures;

// define procedure (sub-routine)
procedure MyProcedure;
var
    // variables are local
    number: integer = 0;
begin
    writeln('number: ', number);
    number += 1;
end;

begin
    MyProcedure;
    // number: 0
    
    MyProcedure;
    // number: 0
end.