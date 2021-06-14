/*
    Mux16(a, b, sel) : If sel = 0 then for i = 0..15 out[i] = a[i] else for i = 0..15 out[i] = b[i]
*/

// gate-level
module mux16_gate (output [15:0] out, input [15:0] a, b, input sel);
    // wire : internal pin
    wire [15:0] w1;
    wire [15:0] w2;
    wire notsel;
    // operations : not
    not(notsel, sel);
    // operations : and : a
    and(w1[0], a[0], notsel);
    and(w1[1], a[1], notsel);
    and(w1[2], a[2], notsel);
    and(w1[3], a[3], notsel);
    and(w1[4], a[4], notsel);
    and(w1[5], a[5], notsel);
    and(w1[6], a[6], notsel);
    and(w1[7], a[7], notsel);
    and(w1[8], a[8], notsel);
    and(w1[9], a[9], notsel);
    and(w1[10], a[10], notsel);
    and(w1[11], a[11], notsel);
    and(w1[12], a[12], notsel);
    and(w1[13], a[13], notsel);
    and(w1[14], a[14], notsel);
    and(w1[15], a[15], notsel);
    // operations : and : b
    and(w2[0], b[0], sel);
    and(w2[1], b[1], sel);
    and(w2[2], b[2], sel);
    and(w2[3], b[3], sel);
    and(w2[4], b[4], sel);
    and(w2[5], b[5], sel);
    and(w2[6], b[6], sel);
    and(w2[7], b[7], sel);
    and(w2[8], b[8], sel);
    and(w2[9], b[9], sel);
    and(w2[10], b[10], sel);
    and(w2[11], b[11], sel);
    and(w2[12], b[12], sel);
    and(w2[13], b[13], sel);
    and(w2[14], b[14], sel);
    and(w2[15], b[15], sel);
    // operations : or
    or(out[0], w1[0], w2[0]);
    or(out[1], w1[1], w2[1]);
    or(out[2], w1[2], w2[2]);
    or(out[3], w1[3], w2[3]);
    or(out[4], w1[4], w2[4]);
    or(out[5], w1[5], w2[5]);
    or(out[6], w1[6], w2[6]);
    or(out[7], w1[7], w2[7]);
    or(out[8], w1[8], w2[8]);
    or(out[9], w1[9], w2[9]);
    or(out[10], w1[10], w2[10]);
    or(out[11], w1[11], w2[11]);
    or(out[12], w1[12], w2[12]);
    or(out[13], w1[13], w2[13]);
    or(out[14], w1[14], w2[14]);
    or(out[15], w1[15], w2[15]);
endmodule

// behavioural-level
module mux16_behavioural (output reg [15:0] out, input [15:0] a, b, input sel);
    always @ (a or b or sel) begin
        // note: 1'b : 1 bit
        if (sel == 1'b0) begin
            out = a;
        end
        else begin
            out = b;
        end
    end
endmodule

// test
module test;
    reg [15:0] a, b;
    reg sel;
    wire [15:0] out;
    
    // mux16_gate Instance0 (out, a, b, sel);
    mux16_behavioural Instance0 (out, a, b, sel);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) a[15:0] = 8'b11111111; b[15:0] = 8'b00000000; sel = 0; // out = 1
        #(1) a[15:0] = 8'b11111111; b[15:0] = 8'b00000000; sel = 1; // out = 0
    end

    initial begin
        $printtimescale;
        // Time scale of (test) is 1s / 1s
        $monitor ("%2d | a = %d | b = %d | sel = %d | out = %d", $time, a[0], b[0], sel, out[0]);
        // 0 | a = 1 | b = 0 | sel = 0 | out = 1
        // 1 | a = 1 | b = 0 | sel = 1 | out = 0
    end
endmodule