/*
    Or(a, b) : If a = b = 0 then out = 0 else out = 1
*/

// gate-level
module or_gate (output out, input a, b);
    // wire : internal pin
    wire w1, w2;
    // operations (note: limited to nand-gates)
    nand(w1, a, a);
    nand(w2, b, b);
    nand(out, w1, w2);
endmodule

// test
module test;
    reg a, b;
    wire out;
    
    or_gate Instance0 (out, a, b);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) a = 0; b = 0; // out = 0
        #(1) a = 0; b = 1; // out = 1
        #(1) a = 1; b = 0; // out = 1
        #(1) a = 1; b = 1; // out = 1
    end

    initial begin
        $printtimescale;
        // Time scale of (_nand_test) is 1s / 1s
        $monitor ("%1d | a = %d | b = %d | out = %d", $time, a, b, out);
        // 0 | a = 0 | b = 0 | out = 0
        // 1 | a = 0 | b = 1 | out = 1
        // 2 | a = 1 | b = 0 | out = 1
        // 3 | a = 1 | b = 1 | out = 1
    end
endmodule