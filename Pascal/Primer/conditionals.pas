// 2020-02
program Conditionals;

const
    ANSWER = 42;
var
    number: integer = 42;
begin
    // single statement in block
    if number = ANSWER then writeln('yes')
    else writeln('no');
    // yes

    // more than one statements in block
    if number = ANSWER then
        begin
            if ANSWER = 42 then
                begin
                    writeln('42 is the answer');
                end
            else
                writeln('42 is not the answer..?');
            // end if
        end
    else
        writeln('no');
    // end if
    // 42 is the answer
end.