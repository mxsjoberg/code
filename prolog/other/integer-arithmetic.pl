/* 
    NOTE: integer arithmetic resources

    - natural numbers: https://en.wikipedia.org/wiki/Peano_axioms
    - successor notation: https://en.wikipedia.org/wiki/Successor_function
*/

% natural_numbers/1
natural_numbers(0).
natural_numbers(s(N)) :-
    natural_numbers(N).

% s(0)          = 1
% s(s(0))       = 2
% ...

?- natural_numbers(s(0)).                       % true.
?- natural_numbers(s(s(0))).                    % true.

% natural_numbers_sum/3
natural_numbers_sum(0, M, M).
natural_numbers_sum(s(N), M, s(Sum)) :-
    natural_numbers_sum(M, N, Sum).

% 1 + 1 = 2 -> s(0) + s(0) = s(s(0))
?- natural_numbers_sum(s(0), s(0), s(s(0))).
% true.

% built-in predicates
:- use_module(library(clpfd)).

% equality: (#=)/2
?- 1 #= 1.                                      % true.

% disequality: (#\=)/2
?- 1 #\= 2.                                     % true.

% less than: (#<)/2
?- 1 #< 2.                                      % true.

% greater than: (#>)/2
?- 1 #> 2.                                      % false.

% integer expressions
?- 1 + 2 #= 7 - 4.                              % true.
?- 1 + 2 #= X - 4.                              % X = 7.
?- 2 * X #= 5.                                  % false.
?- 2 * X #= 4.                                  % X = 2.

% note: (#=)/2 is not same as (=)/2
?- 1 + 2 = 3.                                   % false.

% domain of variable
?- X #\= 1.
% X in inf..0\/2..sup.

% constrain variable to domain
?- X #= 4, X in 1..2.                           % false.
?- X #= 2, X in 1..2.                           % X = 2.

% constrain multiple variables
?- [X, Y] ins 1..2.
% X in 1..2, Y in 1..2.

% labeling: bind a variable to integer in domain
?- X in 0..2, indomain(X).
% X = 0 ;
% X = 1 ;
% X = 2.

?- [X, Y] ins 0..1, label([X, Y]).
% X = Y, Y = 0 ;
% X = 0, Y = 1 ;
% X = 1, Y = 0 ;
% X = Y, Y = 1.

/* EXAMPLE: factorial */

% factorial/2
n_factorial(0, 1).
n_factorial(N, F) :-
    % END: then N has factorial F
    N #> 0,
    % and F is N times F_1
    F #= N * F_1,
    % and N_1 is N - 1
    N_1 #= N - 1,
    % START: if N_1 has factorial F_1
    n_factorial(N_1, F_1).

?- n_factorial(3, F).                           % F = 6 .
?- n_factorial(N, 120).                         % N = 5 .
?- n_factorial(N, F).
% N = 0, F = 1 ;
% N = F, F = 1 ;
% N = F, F = 2 ;
% N = 3, F = 6 ;
% N = 4, F = 24 ;
% N = 5, F = 120 
% ...

/* EXAMPLE: length of list */

% list_length/2
list_length([], 0).
list_length([_|Ls], Length) :-
    % END: then [_|Ls] has length Length 
    % and Length is Length_0 + 1
    Length #= Length_0 + 1,
    % START: if Ls has length Length_0
    list_length(Ls, Length_0).

?- list_length([a, b, c, d], Length).           % Length = 4.
?- list_length(Ls, 3).                          % Ls = [_9006, _9172, _9338] .