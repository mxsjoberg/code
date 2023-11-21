?- X is 10 + 10.                            % X = 20.
?- X is 20 - 10.                            % X = 10.
?- X is 10 * 20.                            % X = 200.
?- X is 20 / 10.                            % X = 2.

% power
?- X is 10 ** 2.                            % X = 100.

% automatic floating point conversion
?- X is (10.0 + (10 + 20)).                 % X = 40.0.
?- X is (20.0 - (10 + 10)).                 % X = 0.0.
?- X is (10.0 * (10 * 2)).                  % X = 200.0.

?- X is (30 / 20).                          % X = 1.5.

% integer division
?- X is (20 // 20).                         % X = 1.
?- X is (30 // 20).                         % X = 1.
?- X is (40 // 20).                         % X = 2.

% modulo, remainder
?- X is mod(12, 10).                        % X = 2.
?- X is mod(10, 20).                        % X = 10.

% common modulo error
?- X is mod(12.5, 10).
% ERROR: Type error: `integer' expected, found `12.5' (a float)

?- X is (mod(round((12.5 * 10)), (10*10)) / 10).
% X = 2.5.

% built in numerical operations
?- X is abs(-20).                           % X = 20.
?- X is min(10, 5).                         % X = 5.
?- X is max(10, 5).                         % X = 10.

% sum, min, max values in list
:- use_module(library(lists)).

?- sum_list([1, 2, 3, 4, 5], X).            % X = 15.
?- min_list([1, 2, 3, 4, 5], X).            % X = 1.
?- max_list([1, 2, 3, 4, 5], X).            % X = 5.

% rounding values
?- X is round(2.945).                       % X = 3.
?- X is round(2.495).                       % X = 2.

% NOTE: equality in expressions
?- 2 + 3 is 6 - 1.                          % false.
?- 2 + 3 =:= 6 - 1.                         % true.

/* EXAMPLE: check if number is even */
is_even(X) :-
    Y is X // 2,
    X =:= 2 * Y.

?- is_even(20).                             % true.
?- is_even(7).                              % false.