:- use_module(library(random)).

?- random(X).                                   % X = 0.3011486766485858.
?- random(0, 100, X).                           % X = 51.

% maybe: succeed/ fail with equal probabilty
?- maybe.                                       % true.
?- maybe.                                       % false.

% maybe/1 (P): succeed/ fail with P probabilty
?- maybe(0.333).                                % false.
?- maybe(0.333).                                % false.
?- maybe(0.333).                                % true.

% random permutation
?- random_perm2(A, B, X, Y).                    % A = X, B = Y.
?- random_perm2(A, B, X, Y).                    % A = Y, B = X.

% random element in list
?- random_member(X, [1, 2, 3, 4, 5]).           % X = 2.

% random select element in list
?- random_select(X, [1, 2, 3, 4, 5], Y).        % X = 3, Y = [1, 2, 4, 5].

% randset/3 (elements, range, list): ordered
?- randset(5, 100, X).                          % X = [30, 35, 51, 59, 73].

% randseq/3 (elements, range, list): unordered
?- randseq(5, 100, X).                          % X = [20, 12, 22, 100, 67].