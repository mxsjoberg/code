% print
?- X = 10.0, print(X).
% 10.0
% X = 10.0.

?- print(a), print(b).
% ab
% true.

% write
?- write('Hello world!'), nl.
% Hello world!
% true.

?- writeln('Hello world!').
% Hello world!
% true.

% format
?- format('Hello ~w!', 'Michael').
% Hello Michael!
% true.

% read
?- read(X), write(X).
% |: 'Michael'.
% Michael
% X = 'Michael'.

/* EXAMPLE: read and welcome user */
hello_user :-
    writeln('Who dis?'),
    read(X),
    format('Hello ~w', [X]).

?- hello_user.
% Who dis?
% |: 'Michael'.
% Hello Michael
% true.

/* EXAMPLE: get ascii value */
get_ascii :-
    writeln('Enter key...'),
    get(X),
    format('Ascii value for ~w is ', [X]),
    put(X), nl.

?- get_ascii.
% Enter key...
% |: A
% Ascii value for 65 is A
% true.