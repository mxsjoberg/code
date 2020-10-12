/*
    NOTE: a set is a list without duplicates
*/

:- use_module(library(lists)).

?- is_set([1, 2, 3, 4, 5]).                     % true.

% convert list to set (discarding duplicates)
?- list_to_set([1, 1, 2, 3, 3, 4, 5], X).       % X = [1, 2, 3, 4, 5].

% intersection
?- intersection([1, 2, 3], [3, 4, 5], X).       % X = [3].

% union
?- union([1, 2, 3], [3, 4, 5], X).              % X = [1, 2, 3, 4, 5].

% subset
?- subset([1, 2], [1, 2, 3, 4, 5]).             % true.

% subtract
?- subtract([1, 2, 3, 4, 5], [4, 5], X).        % X = [1, 2, 3].