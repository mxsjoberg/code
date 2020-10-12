/*
    NOTE: rules

    Head :- Body.
    Head :- G_1, G_2, G_3, ... G_n.

    EXPLANATION: if Body is true, then Head is true, i.e. Body implies Head
*/

% include database
:- include('db.pl').

% three_colors/3 (also defined in 'db.pl')
three_colors(X, Y, Z) :-
    color(X),
    color(Y),
    color(Z),
    format('~w, ~w, and ~w are all colors. ~n', [X, Y, Z]).

% three_colors holds if X is a color AND Y is a color AND Z is a color
?- three_colors(green, red, blue).              % true.
?- three_colors(green, red, black).             % false.

% functional notation (each conjunct is a goal)
','(color(x), ','(color(Y), color(Z))).

% friend_with/2 (also defined in 'db.pl')
friend_with(X, Y) :-
    friend(X, Y),
    format('~w is friend with ~w', [X, Y]).

% who is michael friend with?
?- friend_with(michael, X).
% michael is friend with adam
% X = adam ;
% michael is friend with charlie
% X = charlie.

% mutual_friend/2 (also defined in 'db.pl')
mutual_friend(X, Y) :- 
    friend(X, Y),
    friend(Y, X),
    format('~w and ~w are mutual friends ~n', [X, Y]).

% michael and charlie are mutual friends
?- mutual_friend(michael, charlie).
% false.

% michael and adam are mutual friends
?- mutual_friend(michael, adam).
% michael and adam are mutual friends 
% true 

% who is michael mutual friends with?
?- mutual_friend(michael, X).
% michael and adam are mutual friends 
% X = adam.

/* EXAMPLE: get customer balance */

% customer/3
customer('Michael', 'Smith', 800.55).
customer('Adam', 'Smith', 1200.55).

% get_customer_balance/2
get_customer_balance(First_name, Last_name) :-
    customer(First_name, Last_name, Balance),
    format('Customer: ~w ~w ~nBalance: $~2f ~n', [First_name, Last_name, Balance]).

?- get_customer_balance('Michael', 'Smith').
% Customer: Michael Smith 
% Balance: $800.55 
% true.

/* EXAMPLE: define vertical/ hortizontal lines */

vertical(line(point(X, Y_0), point(X, Y_1))).
hortizontal(line(point(X_0, Y), point(X_1, Y))).

% point A and point B is a vertical line
?- vertical(line(point(2, 8), point(2, 12))).
% true.

% what should point B be to make a hortizontal line
?- hortizontal(line(point(2, 8), point(X, Y))).
% Y = 8.

/* EXAMPLE: determine relations using recursion */

% parent/1
parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).
parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).
parent(bob, carl).
parent(bob, charlie).

% related/2
related(X, Y) :-
    parent(X, Y).
related(X, Y) :-
    % 3. then X is related to Y
    % 2. and X is parent to Z
    parent(X, Z),
    % 1. if Z is related to Y
    related(Z, Y).

% albert is related to carl (albert->bob->carl)
?- related(albert, carl). 
% true .