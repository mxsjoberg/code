% write to file
?- open('test.txt', write, Stream), write(Stream, 'This is a test string.\nSecond line.'), nl, close(Stream).
% Stream = <stream>(0x7fa6514e25e0).

% read a line
?- open('test.txt', read, Stream), read_string(Stream, "\n", "\r", End, String), close(Stream).
% Stream = <stream>(0x7fa653249d30),
% End = 10,
% String = "This is a test string.".

% read until end
?- open('test.txt', read, Stream), read_string(Stream, "\0", "\r", End, String), close(Stream).
% Stream = <stream>(0x7fa651525d30),
% End = -1,
% String = "This is a test string.\nSecond line.".

/* EXAMPLE: write and read from file */

% write to file
write_to_file(File, Text) :-
    open(File, write, Stream),
    write(Stream, Text), nl,
    close(Stream).

read_file(File) :-
    open(File, read, Stream),
    get_char(Stream, Char_0),
    process_stream(Char_0, Stream),
    close(Stream).

process_stream(end_of_file, _) :- !.
process_stream(Char, Stream) :-
    write(Char),
    get_char(Stream, Char_1),
    process_stream(Char_1, Stream).

?- write_to_file('test.txt', 'This is a test string').
% true.

?- read_file('test.txt').
% This is a test string
% true.