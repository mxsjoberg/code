// 2020-02
program InsertionSort;
// https://en.wikipedia.org/wiki/Insertion_sort

var
    i, j, tmp: integer;
    // array of unsorted integers
    numbers: array[0..4] of integer = (14, 33, 27, 35, 10);
begin
    for i := length(numbers) - 1 DownTo 0 do
        begin
            tmp := numbers[i];
            j := i;
            while ((j > 0) and (numbers[j - 1] > tmp)) do
                begin
                    numbers[j] := numbers[j - 1];
                    j -= 1;
                end;
            // end while
            numbers[j] := tmp;
        end;
    // end for

    // sorted
    for i := 0 to length(numbers) - 1 do write(numbers[i], ' ');
    // 10 14 27 33 35
end.