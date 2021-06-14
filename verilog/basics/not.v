/*
    Not(in) : If in = 0 then out = 1 else out = 0
*/

// gate-level
module not_gate (output out, input in);
    // operations (note: limited to nand-gates)
    nand(out, in, in);
endmodule

// test
module test;
    reg in;
    wire out;
    
    not_gate Instance0 (out, in);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) in = 0; // 1
        #(1) in = 1; // 0
    end

    initial begin
        $printtimescale;
        // Time scale of (_nand_test) is 1s / 1s
        $monitor ("%1d | in = %d | out = %d", $time, in, out);
        // 0 | in = 0 | out = 1
        // 1 | in = 1 | out = 0
    end
endmodule