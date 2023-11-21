// 2020-02
program Switch;

var
    numbers: array[0..4] of integer = (1, 2, 3, 42, 5);
    i: integer;
begin
    for i := 0 to length(numbers) - 1 do
        case numbers[i] of
            1: writeln('one');
            2: writeln('two');
            3: writeln('three');
            4: writeln('four');
            5: writeln('five');
        else
            writeln('what?');
        end;
    // end for
    
    // one
    // two
    // three
    // what?
    // five
end.