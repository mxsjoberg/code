% warm_blooded/1
warm_blooded(penguin).
warm_blooded(human).

% produce_milk/1
produce_milk(penguin).
produce_milk(human).

% have_feather/1
have_feather(penguin).

% have_hair/1
have_hair(human).

% mammal/1
mammal(X) :-
    warm_blooded(X),
    produce_milk(X),
    have_hair(X).

/* EXAMPLE: using trace in interactive mode */

?- trace.
% true.

% [trace]  ?- mammal(human).
%    Call: (8) mammal(human) ? creep
%    Call: (9) warm_blooded(human) ? creep
%    Exit: (9) warm_blooded(human) ? creep
%    Call: (9) produce_milk(human) ? creep
%    Exit: (9) produce_milk(human) ? creep
%    Call: (9) have_hair(human) ? creep
%    Exit: (9) have_hair(human) ? creep
%    Exit: (8) mammal(human) ? creep
% true.

% [trace]  ?- mammal(penguin).
%    Call: (8) mammal(penguin) ? creep
%    Call: (9) warm_blooded(penguin) ? creep
%    Exit: (9) warm_blooded(penguin) ? creep
%    Call: (9) produce_milk(penguin) ? creep
%    Exit: (9) produce_milk(penguin) ? creep
%    Call: (9) have_hair(penguin) ? creep
%    Fail: (9) have_hair(penguin) ? creep
%    Fail: (8) mammal(penguin) ? creep
% false.