// 2020-02
program Strings;
uses sysutils, Character;

var
    str: string = 'hello pascal';
begin
    writeln(str);
    // hello pascal
    writeln(str[1]);
    // h
    writeln(str[1..5]);
    // hello

    // length of string
    writeln(length(str));
    // 12

    // built-ins
    writeln(uppercase(str));
    // HELLO PASCAL
    writeln(lowercase(str));
    // hello pascal
    writeln(isnumber(str[1]));
    // FALSE
    writeln(isletter(str[1]));
    // TRUE
    writeln(isupper(str[1]));
    // FALSE
    writeln(islower(str[1]));
    // TRUE
end.