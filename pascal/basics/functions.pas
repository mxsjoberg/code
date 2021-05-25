PROGRAM functions;

// define function
function functionA(x: real; y: real) : real;
BEGIN
    functionA := x * y;
END;
// end function

BEGIN
    WRITELN(functionA(3, 4));
    // 12.0...
END.