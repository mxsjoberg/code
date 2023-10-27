/*
    NOTE: predicates

    - a predicate has a name and arguments, number of arguments is called arity
    - a predicate with name P and N arguments has a predicate indicator: P/N
    - a predicate define a relation between its arguments
    - a predicate is defined by a collection of clauses, a clause is either a rule or a fact
*/

/* built-in predicates */

% true: true/0
% definition: true.
?- true.                                    % true.

% false: false/0
% definition: false :- 0 = 1.
?- false.                                   % false.

% conjunction (AND): (',')/2
?- ','(true, true).                         % true.
?- ','(true, false).                        % false.

% disjunction (OR): (;)/2
% definition: 
%   (A ; _) :- A.
%   (_ ; B) :- B.
?- ;(true, false).                          % true

% unification (=): (=)/2
% definition: X = X.
?- =(1, 1).                                 % true.
?- =(1, 2).                                 % false.

% disequality (!=): dif/2
?- dif(1, 2).                               % true.