PROGRAM insertion_sort;
VAR
    i, j, tmp: integer;

    // array of unsorted integers
    numbers: array[0..4] of integer = (14, 33, 27, 35, 10);
BEGIN
    // https://en.wikipedia.org/wiki/Insertion_sort
    for i := LENGTH(numbers) - 1 DownTo 0 do
        BEGIN
            tmp := numbers[i];
            j := i;

            while ((j > 0) and (numbers[j - 1] > tmp)) do
                BEGIN
                    numbers[j] := numbers[j - 1];
                    j -= 1;
                END;
            // end while
            numbers[j] := tmp;
        END;
    // end for

    // sorted
    for i := 0 to LENGTH(numbers) - 1 do WRITELN(numbers[i]);
    // 10
    // 14
    // 27
    // 33
    // 35
END.