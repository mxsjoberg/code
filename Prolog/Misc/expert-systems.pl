/*
    NOTE: an expert systems derive useful new information based on user-provided input

    https://www.metalevel.at/prolog/expertsystems
*/

/*
    EXAMPLE: animal identification
    
    - if it has fur and says woof, then the animal is dog
    - if it has fur and says meow, then the animal is cat
    - if it has feathers and says quack, then the animal is duck
*/

animal(dog) :- is_true('has fur'), is_true('says woof').
animal(cat) :- is_true('has fur'), is_true('says meow').
animal(duck) :- is_true('has feathers'), is_true('says quack').

is_true(Q) :-
    format('~w\n', [Q]),
    read(yes).

?- animal(A).
% has fur
% |: yes.
% says woof
% |: yes.
% 
% A = dog .

% note that questions are asked more than once
?- animal(B).
% has fur
% |: no.
% has fur
% |: yes.
% says meow
% |: yes.
% 
% B = cat .

% using a domain-specific-language/ binary tree

tree(if_then_else('has fur',
        if_then_else('says woof',
            animal(dog),
            if_then_else('says meow',
                animal(cat),
                false)),
        if_then_else('has feathers',
            if_then_else('says quack',
                animal(duck),
                false),
            false))).

animal(A) :-
    tree(T),
    tree_animal(T, A).

tree_animal(animal(A), A).
tree_animal(if_then_else(Condition, Then, Else), A) :-
    (   is_true(Condition) ->
        tree_animal(Then, A)
    ;   tree_animal(Else, A)
    ).

?- animal(A).
% has fur
% |: yes.
% says woof
% |: no.
% says meow
% |: yes.
%
% A = cat.