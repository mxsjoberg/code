PROGRAM files;
VAR
    f: file of string;

    // variable for text
    text: string;
BEGIN
    // write to file
    ASSIGN(f, 'test.txt');
    REWRITE(f);
    WRITE(f, 'hello pascal');
    CLOSE(f);

    // read from file
    ASSIGN(f, 'test.txt');
    RESET(f);
    while not EOF(f) do
        BEGIN
            READ(f,text);
            WRITELN(text);
        END;
    // end while
    CLOSE(f);
    // hello pascal
END.