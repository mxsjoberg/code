/*
    NOTE: a list is divided into head and tail

    Head|Tail
    H|T
*/

/*
    lists are defined inductively:

    - the atom [] (nil) is the empty list
    - the compound term .(H, T) is a list iff T is a list
    - '.'/2 is called list constructor
*/

:- use_module(library(lists)).

% represent strings as lists of characters
:- set_prolog_flag(double_quotes, chars).

% list/1, empty list
list([]).

% list/1, list of characters
list("hello world").

% list/1, list of integers
list([1, 2, 3, [4, 5]]).

?- list(X).
% X = [] ;
% X = [h, e, l, l, o, ' ', w, o, r|...] ;
% X = [1, 2, 3, [4, 5]].

% get head and tail
?- [H|T] = [1, 2, 3, [4, 5]].
% H = 1,
% T = [2, 3, [4, 5]].

% get head, ignore tail
?- [H|_] = [1, 2, 3, [4, 5]].
% H = 1.

% get specific elements
?- [_, _, _, [X, _]|_] = [1, 2, 3, [4, 5]].
% X = 4.

% add element to list
?- write([0|[1, 2, 3]]).
% [0,1,2,3]
% true.

% check if element in list
?- member(d, [a, b, c]).                        % false.
?- member(c, [a, b, c]).                        % true.

% iterate all elements in list
?- member(X, [a, b, c]).
% X = a ;
% X = b ;
% X = c.

% get element n in list
?- nth0(0, [1, 2, 3, [4, 5]], X).               % X = 1.
?- nth0(1, [1, 2, 3, [4, 5]], X).               % X = 2.

% last element in list
?- last([1, 2, 3, [4, 5]], X).                  % X = [4, 5].

% append
?- append([1, 2, 3], [4, 5], X).                % X = [1, 2, 3, 4, 5].
?- append([1, 2, 3, 4, 5], [6], X).             % X = [1, 2, 3, 4, 5, 6].

% delete
?- delete([1, 2, 3, 4, 5, 6], 6, X).            % X = [1, 2, 3, 4, 5].

% length of list
?- length([1, 2, 3], X).                        % X = 3.
?- proper_length("hello world", X).             % X = 11.

% reverse list
?- reverse("hello world", X).                   % X = [d, l, r, o, w, ' ', o, l, l|...].

% sort list
?- sort([2, 5, 1, 3, 4], X).                    % X = [1, 2, 3, 4, 5].

% permutations
?- permutation([a, b, c], X).
% X = [a, b, c] ;
% X = [a, c, b] ;
% X = [b, a, c] ;
% X = [b, c, a] ;
% X = [c, a, b] ;
% X = [c, b, a] ;
% false.

% flatten
?- flatten([1, 2, 3, [4, 5]], X).               % X = [1, 2, 3, 4, 5].

% intersection
?- intersection([1, 2, 3], [3, 4, 5], X).       % X = [3].

% union
?- union([1, 2, 3], [3, 4, 5], X).              % X = [1, 2, 3, 4, 5].

/* EXAMPLE: recursive rule to iterate list */

% iterate_list/1
iterate_list([]).
iterate_list([Head|Tail]) :- 
    writeln(Head),
    iterate_list(Tail).

?- X = "Michael", iterate_list(X).
% M
% i
% c
% h
% a
% e
% l
% false.

% increment_list/1
increment_list([]).
increment_list([Head|Tail], Result) :- 
    X is (Head + 1),
    append(Result, [X], Y),
    writeln(Y),
    increment_list(Tail, Y).

?- increment_list([1, 2, 3, 4], []).
% [2]
% [2,3]
% [2,3,4]
% [2,3,4,5]
% false.