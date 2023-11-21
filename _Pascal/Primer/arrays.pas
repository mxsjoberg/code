// 2020-02
program Arrays;

type
    // define type for array[20] of real
    default_array = array[0..19] of real;
var
    // declare variable using default array type
    arr: default_array;
    // declare array without default type
    vector: array[0..4] of integer;
    // nd-array
    matrix: array[0..9, 0..9] of integer;
    // declare and populate
    numbers: array[0..4] of integer = (1, 2, 3, 4, 5);
    // declare iterators
    i, j: integer;
begin
    // populate array
    for i := 0 to 19 do arr[i] := i;
    // access element
    writeln(arr[0]);
    // 0.0...
    writeln(arr[8]);
    // 8.0...
    
    // iterate array
    for i := 0 to length(numbers) - 1 do writeln(numbers[i]);
    // 1
    // 2
    // 3
    // 4
    // 5

    // populate nd-array
    for i := 0 to 9 do
        for j := 0 to 9 do
            matrix[i, j] := i + j;

    // access element in nd-array
    writeln(matrix[0, 0]);
    // 0
    writeln(matrix[3, 3]);
    // 6

    // length of first dimension
    writeln(length(matrix));
    // 10
end.