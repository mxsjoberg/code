// 2020-02
program Files;

var
    // variable for file
    f: file of string;
    // variable for text
    text: string;
begin
    // write to file
    assign(f, '_file.txt');
    rewrite(f);
    write(f, 'hello pascal');
    close(f);

    // read from file
    assign(f, '_file.txt');
    reset(f);
    while not eof(f) do
        begin
            read(f, text);
            writeln(text);
        end;
    // end while
    close(f);
    // hello pascal
end.