% constants
?- X is pi.                             % X = 3.141592653589793.
?- X is e.                              % X = 2.718281828459045.

/* numerical operations */

% floor
?- X is floor(2.945).                   % X = 2.

% truncate
?- X is truncate(2.945).                % X = 2.

% exp
?- X is exp(1).                         % X = 2.718281828459045.

% sqrt
?- X is sqrt(16).                       % X = 4.0.

/* EXAMPLE: trigonometric expression */
?- X is sin(4 * pi / 180).
% X = 0.0697564737441253.

% find more at: https://www.swi-prolog.org/pldoc/man?section=functions