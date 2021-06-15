/*
    Nand(a, b) : If a = b = 1 then out = 0 else out = 1
*/

// gate-level
module nand_gate (output out, input a, b);
    // wire : internal pin
    wire w;
    // operations
    and(w, a, b);
    not(out, w);
endmodule

// behavioural-level
module nand_behavioural (output reg out, input a, b);
    always @ (a or b) begin
        // note: 1'b : 1 bit
        if (a == 1'b1 & b == 1'b1) begin
            out = 1'b0;
        end
        else begin
            out = 1'b1;
        end
    end
endmodule

// test
module test;
    reg a, b;
    wire out;
    
    // nand_gate Instance0 (out, a, b);
    nand_behavioural Instance0 (out, a, b);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) a = 0; b = 0; // 1
        #(1) a = 0; b = 1; // 1
        #(1) a = 1; b = 0; // 1
        #(1) a = 1; b = 1; // 0
    end

    initial begin
        $printtimescale;
        // Time scale of (_nand_test) is 1s / 1s
        $monitor ("%1d | a = %d | b = %d | out = %d", $time, a, b, out);
        // 0 | a = 0 | b = 0 | out = 1
        // 1 | a = 0 | b = 1 | out = 1
        // 2 | a = 1 | b = 0 | out = 1
        // 3 | a = 1 | b = 1 | out = 0
    end
endmodule