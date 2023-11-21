/* 
    NOTE: facts

    - a fact is a statement that describe object properties or relations between objects
    - all forms of data are called terms and each term is either a variable, an atomic term or a compound term
    - facts and rules are conventionally stored in a database, such as 'db.pl' (see source on github)
*/

/*
    Head.
    Head :- true.

    variable        : starts with uppercase or _, single _ is anonymous variable

    atomic term:
    - atom          : starts with lowercase, e.g. a, at, atom, 'Name'
    - integer       : 12, 100, 2_020
    - others        : 3.1415

    compound term   : P/N
*/

% color/1
color(red).
color(green).
color(blue).

% NOTE: color holds if X is red OR green OR blue
?- color(green).                                % true.
?- color(black).                                % false.

% additional facts
male(michael).                                  % michael is male
friend(michael, adam).                          % michael is friend with adam

?- male(michael).                               % true.
?- friend(michael, X).                          % X = adam.

% compound terms: atom and compound term
person(michael, nationality(sweden, swedish)).
person(adam, nationality(norway, norwegian)).

?- person(michael, nationality(X, Y)).          % X = sweden, Y = swedish.
?- person(X, nationality(sweden, _)).           % X = michael

% type tests
?- must_be(atom, a).                            % true.
?- must_be(atom, 2).                            % ERROR: Type error: `atom' expected, found `2' (an integer)
?- must_be(integer, 2).                         % true.

% term inspection
?- functor(f(a, g(X)), Functor, Arity).         % Functor = f, Arity = 2.

% canonical representation
?- write_canonical(a + b = [x, y, z]).          % =(+(a,b),[x,y,z]) true.