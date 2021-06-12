/*
    Xor(a, b) : If a<>b then out = 1 else out = 0
*/

// gate-level
module xor_gate (output out, input a, b);
    // wire : internal pin
    wire w1;
    wire w2;
    wire nota;
    wire notb;
    // operations
    not(nota, a);
    not(notb, b);
    and(w1, a, notb);
    and(w2, nota, b);
    or(out, w1, w2);
endmodule

// behavioural-level
module xor_behavioural (output reg out, input a, b);
    always @ (a or b) begin
        // note: 1'b : 1 bit
        if ((a == 1'b1 & b == 1'b0) | (a == 1'b0 & b == 1'b1)) begin
            out = 1'b1;
        end
        else begin
            out = 1'b0;
        end
    end
endmodule

// test
module test;
    reg a, b;
    wire out;
    
    // xor_gate Instance0 (out, a, b);
    xor_behavioural Instance0 (out, a, b);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) a = 0; b = 0; // 0
        #(1) a = 0; b = 1; // 1
        #(1) a = 1; b = 0; // 1
        #(1) a = 1; b = 1; // 0
    end

    initial begin
        $printtimescale;
        // Time scale of (test) is 1s / 1s
        $monitor ("%1d | a = %d | b = %d | out = %d", $time, a, b, out);
        // 0 | a = 0 | b = 0 | out = 0
        // 1 | a = 0 | b = 1 | out = 1
        // 2 | a = 1 | b = 0 | out = 1
        // 3 | a = 1 | b = 1 | out = 0
    end
endmodule