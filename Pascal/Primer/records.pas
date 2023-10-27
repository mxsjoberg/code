// 2020-02
program Records;

type
    // define record type
    Element = record
        text: string;
        numbers: array[0..4] of integer;
        val: real;
    end;
var
    First, Second: Element;
begin
    First.text := 'this is my first element';
    First.numbers[0] := 1;
    First.numbers[1] := 2;
    First.val := 3.14;

    writeln(First.text);
    // this is my first element
    writeln(First.numbers[1]);
    // 2
    writeln(First.val);
    // 3.14...

    // with
    with Second do
    begin
        text := 'this is my second element';
        numbers[0] := 6;
        numbers[1] := 7;
        numbers[2] := 8;
        numbers[3] := 9;
        val := -12.5;
    end;

    writeln(Second.text);
    // this is my second element
    writeln(Second.numbers[3]);
    // 9
    writeln(Second.val);
    // -12.5...
end.