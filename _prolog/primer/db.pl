/*** db ***/

/* colors */

% color/1
color(red).
color(green).
color(blue).

% three_colors/3
three_colors(X, Y, Z) :-
    color(X),
    color(Y),
    color(Z),
    format('~w, ~w, and ~w are all colors. ~n', [X, Y, Z]).

/* persons */

% person/2
person(michael, nationality(sweden, swedish)).
person(adam, nationality(norway, norwegian)).
person(charlie, nationality(england, english)).

% male/1
male(michael).
male(adam).
male(charlie).

% friend/1
friend(michael, adam).
friend(adam, michael).
friend(michael, charlie).

% friend_with/2
friend_with(X, Y) :-
    friend(X, Y),
    format('~w is friend with ~w', [X, Y]).

% mutual_friend/2
mutual_friend(X, Y) :- 
    friend(X, Y),
    friend(Y, X),
    format('~w and ~w are mutual friends ~n', [X, Y]).