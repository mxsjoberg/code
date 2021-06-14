/*
    Not16(in, out) : For i = 0..15 out[i] = Not(in[i])
*/

// gate-level
module not16_gate (output [15:0] out, input [15:0] in);
    // operations
    not(out[0], in[0]);
    not(out[1], in[1]);
    not(out[2], in[2]);
    not(out[3], in[3]);
    not(out[4], in[4]);
    not(out[5], in[5]);
    not(out[6], in[6]);
    not(out[7], in[7]);
    not(out[8], in[8]);
    not(out[9], in[9]);
    not(out[10], in[10]);
    not(out[11], in[11]);
    not(out[12], in[12]);
    not(out[13], in[13]);
    not(out[14], in[14]);
    not(out[15], in[15]);
endmodule

// behavioural-level
module not16_behavioural (output reg [15:0] out, input [15:0] in);
    always @ (in) begin
        // note: 1'b : 1 bit 
        out = ~in;
    end
endmodule

// test
module test;
    integer i;
    reg [15:0] in;
    wire [15:0] out;

    // not16_gate Instance0 (out, in);
    not16_behavioural Instance0 (out, in);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) in[8:0]    = 8'b11111111; // 0, 0, 0, 0, 0, 0, 0, 0
        #(1) in[15:8]   = 8'b00000000; // 1, 1, 1, 1, 1, 1, 1, 1
    end

    initial begin
        $printtimescale;
        // Time scale of (test) is 1s / 1s
        #(0) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[0], out[0]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[1], out[1]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[2], out[2]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[3], out[3]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[4], out[4]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[5], out[5]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[6], out[6]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[7], out[7]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[8], out[8]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[9], out[9]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[10], out[10]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[11], out[11]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[12], out[12]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[13], out[13]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[14], out[14]);
        #(1) $monitor ("%2d | in[%2d] = %d | out = %d", $time, $time, in[15], out[15]);
        //  0 | in[ 0] = 1 | out = 0
        //  1 | in[ 1] = 1 | out = 0
        //  2 | in[ 2] = 1 | out = 0
        //  3 | in[ 3] = 1 | out = 0
        //  4 | in[ 4] = 1 | out = 0
        //  5 | in[ 5] = 1 | out = 0
        //  6 | in[ 6] = 1 | out = 0
        //  7 | in[ 7] = 1 | out = 0
        //  8 | in[ 8] = 0 | out = 1
        //  9 | in[ 9] = 0 | out = 1
        // 10 | in[10] = 0 | out = 1
        // 11 | in[11] = 0 | out = 1
        // 12 | in[12] = 0 | out = 1
        // 13 | in[13] = 0 | out = 1
        // 14 | in[14] = 0 | out = 1
        // 15 | in[15] = 0 | out = 1
    end
endmodule