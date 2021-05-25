PROGRAM strings;
USES sysutils, Character;
VAR
    str: string = 'hello pascal';
BEGIN
    WRITELN(str);                   // hello pascal
    WRITELN(str[1]);                // h
    WRITELN(str[1..5]);             // hello

    // length
    WRITELN(LENGTH(str));
    // 12

    // built-ins
    WRITELN(UPPERCASE(str));        // HELLO PASCAL
    WRITELN(LOWERCASE(str));        // hello pascal

    // conditionals
    WRITELN(ISNUMBER(str[1]));      // FALSE
    WRITELN(ISLETTER(str[1]));      // TRUE
    WRITELN(ISUPPER(str[1]));       // FALSE
    WRITELN(ISLOWER(str[1]));       // TRUE
END.