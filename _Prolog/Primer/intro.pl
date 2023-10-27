/*
    Prolog is a logic programming language developed by Alain Colmerauer and Robert Kowalski in 1972.

    https://en.wikipedia.org/wiki/Prolog
*/

% include database (collection of facts)
:- include('db.pl').

% initialise main 
:- initialization main.

main :- 
    % do something
    halt.

/*  
    build and run from command-line: SWI-Prolog CLI

    - interactive mode                  : $ swipl
    - load file                         : ?- consult('filename.pl').
        or                              : ?- ['filename.pl'].
        or                              : $ swipl filename.pl
    - load multiple files               : ?- ['filename.pl', 'filename.pl']
    - list all clauses in database      : ?- listing.
    - list specific clauses             : ?- listing(character/2).
*/