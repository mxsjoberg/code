// 2020-02
program Logicals;

const
    YES: boolean = true;
    NO: boolean = false;
begin
    writeln(YES or NO);
    // TRUE
    writeln(YES and (YES and NO));
    // FALSE
    writeln(not YES);
    // FALSE
    writeln(not (not YES));
    // TRUE

    writeln(1 = 1);
    // TRUE
    writeln(1 <> 1);
    // FALSE
    writeln(1 > 0);
    // TRUE
    writeln(1 < 0);
    // FALSE
    writeln(1 >= 1);
    // TRUE
    writeln(1 <= 0);
    // FALSE
end.