PROGRAM arrays;
TYPE
    // define array type
    default = array[0..19] of real;
VAR
    // declare variable
    lst: default;

    // declare without type
    vector: array[0..4] of integer;

    // n-dimensional
    matrix: array[0..9, 0..9] of integer;

    // declare and initialise
    numbers: array[0..4] of integer = (1, 2, 3, 4, 5);

    // declare iterator variables
    i, j: integer;
BEGIN
    // initialise array
    for i := 0 to 19 do lst[i] := i;

    // access element in array
    WRITELN(lst[0]);                            // 0.0...
    WRITELN(lst[8]);                            // 8.0...

    // iterate array
    for i := 0 to 4 do WRITELN(numbers[i]);
    // 1
    // 2
    // 3
    // 4
    // 5

    // initialise n-dimensional array
    for i := 0 to 9 do
        for j := 0 to 9 do
            matrix[i, j] := i + j;

    // access element in n-dimensional array
    WRITELN(matrix[0, 0]);                      // 0
    WRITELN(matrix[3, 3]);                      // 6

    // length of array
    WRITELN(length(lst));                       // 20
    WRITELN(length(matrix));                    // 10
END.