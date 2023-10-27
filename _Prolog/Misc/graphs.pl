% vertex/1
:- dynamic vertex/1.
vertex('A').
vertex('B').
vertex('C').
vertex('D').

?- vertex(X).
% X = 'A' ;
% X = 'B' ;
% X = 'C' ;
% X = 'D'.

% edge/2
:- dynamic edge/2.
edge('A', 'B').
edge('B', 'A').

edge('A', 'C').
% edge('C', 'A').

edge('C', 'D').
edge('D', 'C').

?- edge('A', X).
% X = 'B' ;
% X = 'C'.

% graph/1
:- dynamic graph/1.
graph(['A', 'B', 'C', 'D']).

?- graph(X).
% X = ['A', 'B', 'C', 'D'].

% undirected_edge/2
undirected_edge(X, Y) :-
    edge(X, Y),
    edge(Y, X).

?- undirected_edge('A', X).
% X = 'B' ;
% false.

% remove_edge/2
remove_edge(X, Y) :-
    edge(X, Y),
    retract(edge(X, Y)).

?- remove_edge('A', 'B').
% true ;
% false.

?- edge('A', 'B').
% false.