/*
    NOTE: directives are predicates to run at load time

    :- Body.
*/

% include database
:- include('db.pl').

% directive to include file
% :- include('filename.pl').

:- X = green, color(X), format('~w is a color.', [X]).
% green is a color.

:- X = boat, color(X), format('~w is a color.', [X]).
% Goal (directive) failed: ...

:- X = sweden, person(Y, nationality(X, _)), format('~w is from ~w.', [Y, X]).
% michael is from sweden.

:- X = michael, friend_with(X, Y).
% michael is friend with adam