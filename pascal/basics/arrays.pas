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

    // declare iterator variables
    i, j: integer;
BEGIN
    // initialise array
    for i := 0 to 19 do
        lst[i] := i;

    // access element in array
    WRITELN(lst[0]);                            // 0
    WRITELN(lst[8]);                            // 8

    // iterate array (note: one line is ok)
    for i := 0 to 4 do vector[i] := i * i;
    for j := 0 to 4 do WRITELN(vector[j]);
    // 0
    // 1
    // 4
    // 9
    // 16

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