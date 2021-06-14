/*
    And16(a, b) : For i = 0..15 out[i] = And(a[i], b[i])
*/

// gate-level
module and16_gate (output [15:0] out, input [15:0] a, b);
    // operations
    and(out[0], a[0], b[0]);
    and(out[1], a[1], b[1]);
    and(out[2], a[2], b[2]);
    and(out[3], a[3], b[3]);
    and(out[4], a[4], b[4]);
    and(out[5], a[5], b[5]);
    and(out[6], a[6], b[6]);
    and(out[7], a[7], b[7]);
    and(out[8], a[8], b[8]);
    and(out[9], a[9], b[9]);
    and(out[10], a[10], b[10]);
    and(out[11], a[11], b[11]);
    and(out[12], a[12], b[12]);
    and(out[13], a[13], b[13]);
    and(out[14], a[14], b[14]);
    and(out[15], a[15], b[15]);
endmodule

// behavioural-level
module and16_behavioural (output reg [15:0] out, input [15:0] a, b);
    always @ (a or b) begin
        out = a & b;
    end
endmodule

// test
module test;
    reg [15:0] a, b;
    wire [15:0] out;

    // and16_gate Instance0 (out, a, b);
    and16_behavioural Instance0 (out, a, b);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        a[7:0] = 8'b11111111; b[7:0] = 8'b11111111;     // 1, 1, 1, 1, 1, 1, 1, 1
        a[15:8] = 8'b00000000; b[15:8] = 8'b11111111;   // 0, 0, 0, 0, 0, 0, 0, 0
    end

    initial begin
        $printtimescale;
        // Time scale of (test) is 1s / 1s
        #(0) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[0], b[0], out[0]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[1], b[1], out[1]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[2], b[2], out[2]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[3], b[3], out[3]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[4], b[4], out[4]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[5], b[5], out[5]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[6], b[6], out[6]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[7], b[7], out[7]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[8], b[8], out[8]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[9], b[9], out[9]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[10], b[10], out[10]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[11], b[11], out[11]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[12], b[12], out[12]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[13], b[13], out[13]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[14], b[14], out[14]);
        #(1) $monitor ("%2d | a = %d | b = %d | out = %d", $time, a[15], b[15], out[15]);
        //  0 | a = 1 | b = 1 | out = 1
        //  1 | a = 1 | b = 1 | out = 1
        //  2 | a = 1 | b = 1 | out = 1
        //  3 | a = 1 | b = 1 | out = 1
        //  4 | a = 1 | b = 1 | out = 1
        //  5 | a = 1 | b = 1 | out = 1
        //  6 | a = 1 | b = 1 | out = 1
        //  7 | a = 1 | b = 1 | out = 1
        //  8 | a = 0 | b = 1 | out = 0
        //  9 | a = 0 | b = 1 | out = 0
        // 10 | a = 0 | b = 1 | out = 0
        // 11 | a = 0 | b = 1 | out = 0
        // 12 | a = 0 | b = 1 | out = 0
        // 13 | a = 0 | b = 1 | out = 0
        // 14 | a = 0 | b = 1 | out = 0
        // 15 | a = 0 | b = 1 | out = 0
    end
endmodule
