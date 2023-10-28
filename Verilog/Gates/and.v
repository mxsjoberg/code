/*
    And(a, b) : If a = b = 1 then out = 1 else out = 0
*/

// gate-level
module and_gate (output out, input a, b);
    // wire : internal pin
    wire w;
    // operations (note: limited to nand-gates)
    nand(w, a, b);
    nand(out, w, w);
endmodule

// test
module test;
    reg a, b;
    wire out;
    
    and_gate Instance0 (out, a, b);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) a = 0; b = 0; // 0
        #(1) a = 0; b = 1; // 0
        #(1) a = 1; b = 0; // 0
        #(1) a = 1; b = 1; // 1
    end

    initial begin
        $printtimescale;
        // Time scale of (_nand_test) is 1s / 1s
        $monitor ("%1d | a = %d | b = %d | out = %d", $time, a, b, out);
        // 0 | a = 0 | b = 0 | out = 0
        // 1 | a = 0 | b = 1 | out = 0
        // 2 | a = 1 | b = 0 | out = 0
        // 3 | a = 1 | b = 1 | out = 1
    end
endmodule