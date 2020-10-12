/*
    NOTE: a query is a goal to prove

    ?- Head.
*/

% include database
:- include('db.pl').

% green is a color
?- color(green).                                    % true.

% michael is male
?- male(michael).                                   % true.

% a query fails if goal is not provable
% even if true
?- color(boat).                                     % false. (this is correct)
?- color(black).                                    % false. (but should be true, description is incomplete)

% equality
?- =(a, b).                                         % false.
?- a = b.                                           % false.
?- a = a.                                           % true.

% note: atom = atom, but atom /= list
?- 'michael' = michael.                             % true.
?- "michael" = michael.                             % false.

% disequality
?- "michael" \= michael.                            % true.

% greater/ less than or equal
?- 5 >= 10.                                         % false.
?- 5 =< 10.                                         % true.

% assignment
?- X = 5.                                           % X = 5.

% assignment and conditional
?- X = 5, X =< 10.                                  % false.

% substitution
?- expression(10, Y) = expression(X, 2).            % Y = 2, X = 10.

% compound queries: all goals need to be true
?- male(michael), friend(michael, adam).            % true 

% queries using logical variables
?- color(X).                                        % X = red ; X = green ; X = blue ;
?- person(michael, nationality(X, Y)).              % X = sweden, Y = swedish.

% anonymous variables (ignoring values)
?- person(X, nationality(sweden, _)).               % X = michael

% conditional solutions
?- dif( f(g(X)), f(g(Y)) ).                         % dif(Y, X).