recursive_function(0) :- writeln('Done'), halt.
recursive_function(X) :-
    % do something
    writeln(X),
    Y is X - 1,
    recursive_function(Y).

?- recursive_function(2).
% 2
% 1
% Done

/* EXAMPLE: count to N starting at S */

count_to(N, S) :- 
    N =:= S,
    writeln(N),
    writeln('Done'),
    halt.

count_to(N, S) :-
    writeln(S),
    X is S + 1,
    count_to(N, X).

?- count_to(6, 2).
% 2
% 3
% 4
% 5
% 6
% Done

/* EXAMPLE: guess number loop */

guess_number :- loop(begin).

loop(begin) :- 
    writeln('Guess number: '),
    read(Guess),
    loop(Guess).
loop(42) :- writeln('Correct!').
loop(X) :- 
    X \= 42,
    format('~w is not correct.', [X]), nl,
    loop(begin).

?- guess_number.
% Guess number: 
% |: 5.
% 5 is not correct.
% Guess number: 
% |: 42.
% Correct!
% true .