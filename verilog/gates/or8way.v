/*
    Or8Way(in) : out = Or(in[0], ..., in[7])
*/

// gate-level
module or8way_gate (output out, input [7:0] in);
    // operations : or
    or(out, in[0], in[1], in[2], in[3], in[4], in[5], in[6], in[7]);
endmodule

// behavioural-level
module or8way_behavioural (output reg out, input [7:0] in);
    always @ (in) begin
        out = in[0] | in[1] | in[2] | in[3] | in[4] | in[5] | in[6] | in[7];
    end
endmodule

// test
module test;
    reg [7:0] in;
    wire out;
    
    // or8way_gate Instance0 (out, in);
    or8way_behavioural Instance0 (out, in);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) in[0] = 1; in[1] = 0; in[2] = 1; in[3] = 0; in[4] = 1; in[5] = 0; in[6] = 1; in[7] = 0; // out = 1
        #(1) in[0] = 0; in[1] = 0; in[2] = 0; in[3] = 0; in[4] = 0; in[5] = 0; in[6] = 0; in[7] = 0; // out = 0
    end

    initial begin
        $printtimescale;
        // Time scale of (_nand_test) is 1s / 1s
        $monitor ("%1d | in = [%d, %d, %d, %d, %d, %d, %d, %d] | out = %d", $time, in[0], in[1], in[2], in[3], in[4], in[5], in[6], in[7], out);
        // 0 | in = [1, 0, 1, 0, 1, 0, 1, 0] | out = 1
        // 1 | in = [0, 0, 0, 0, 0, 0, 0, 0] | out = 0
    end
endmodule