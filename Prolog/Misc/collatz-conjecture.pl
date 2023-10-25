/*
    Collatz Conjecture: no matter what value of N, the specified sequence will always reach 1.

    For any positive integer N, to get next integer, do:
    
    - if N is even, divide by 2
    - if N is odd, multiply by 3 and add 1, i.e 3xN + 1

    Repeat indefinitely to obtain the hailstone sequence N_0, N_1, N_2, ...

    https://en.wikipedia.org/wiki/Collatz_conjecture
*/

:- use_module(library(clpfd)).

hailstone(N, N).

hailstone(N_0, N) :-
    N_0 #= 2 * N_1,
    hailstone(N_1, N).

hailstone(N_0, N) :-
    N_0 #= 2 * _ + 1,
    N_1 #= 3 * N_0 + 1,
    hailstone(N_1, N).

%:- hailstone(3, N), print(N), nl, N = 1.

:- initialization main.

main :- 
    hailstone(3, N), print(N), nl, N = 1,

    halt.

% N = 3
% N = 10
% N = 5
% N = 16
% N = 8
% N = 4
% N = 2
% N = 1