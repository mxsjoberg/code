PROGRAM bubble_sort;
VAR
    i, j, tmp: integer;

    // array of unsorted integers
    numbers: array[0..4] of integer = (14, 33, 27, 35, 10);
BEGIN
    // https://en.wikipedia.org/wiki/Bubble_sort
    for i := LENGTH(numbers) - 1 DownTo 0 do
        for j := LENGTH(numbers) - 2 DownTo 0 do
            if (numbers[j] > numbers[j + 1]) then
                BEGIN
                    tmp := numbers[j];
                    // swap positions
                    numbers[j] := numbers[j + 1];
                    numbers[j + 1] := tmp;
                END;
            // end if
        // end for
    // end for

    // sorted
    for i := 0 to LENGTH(numbers) - 1 do WRITELN(numbers[i]);
    // 10
    // 14
    // 27
    // 33
    // 35
END.