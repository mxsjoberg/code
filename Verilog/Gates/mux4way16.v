/*
    Mux4Way16(a, b, c, d, sel) :
        If sel = 00 then out = a else if
           sel = 01 then out = b else if
           sel = 10 then out = c else if
           sel = 11 then out = d
*/

// mux.v
module mux_gate (output out, input a, b, sel);
    // wire : internal pin
    wire w1;
    wire w2;
    wire notsel;
    // operations
    not(notsel, sel);
    and(w1, a, notsel);
    and(w2, b, sel);
    or(out, w1, w2);
endmodule

// mux16.v
module mux16_gate (output [15:0] out, input [15:0] a, b, input sel);
    mux_gate Instance0 (out[0], a[0], b[0], sel);
    mux_gate Instance1 (out[1], a[1], b[1], sel);
    mux_gate Instance2 (out[2], a[2], b[2], sel);
    mux_gate Instance3 (out[3], a[3], b[3], sel);
    mux_gate Instance4 (out[4], a[4], b[4], sel);
    mux_gate Instance5 (out[5], a[5], b[5], sel);
    mux_gate Instance6 (out[6], a[6], b[6], sel);
    mux_gate Instance7 (out[7], a[7], b[7], sel);
    mux_gate Instance8 (out[8], a[8], b[8], sel);
    mux_gate Instance9 (out[9], a[9], b[9], sel);
    mux_gate Instance10 (out[10], a[10], b[10], sel);
    mux_gate Instance11 (out[11], a[11], b[11], sel);
    mux_gate Instance12 (out[12], a[12], b[12], sel);
    mux_gate Instance13 (out[13], a[13], b[13], sel);
    mux_gate Instance14 (out[14], a[14], b[14], sel);
    mux_gate Instance15 (out[15], a[15], b[15], sel);
endmodule

// gate-level
module mux4way16_gate (output [15:0] out, input [15:0] a, b, c, d, input [1:0] sel);
    wire [15:0] ab, cd;

    mux16_gate Instance0 (ab, a, b, sel[1]);
    mux16_gate Instance1 (cd, c, d, sel[1]);
    mux16_gate Instance2 (out, ab, cd, sel[0]);
endmodule

// behavioural-level
module mux4way16_behavioural (output reg [15:0] out, input [15:0] a, b, c, d, input [1:0] sel);
    always @ (a or b or c or d or sel) begin
        // note: 2'b : 2 bit
        if (sel == 2'b00) begin
            out = a;
        end
        else if (sel == 2'b10) begin
            out = b;
        end
        else if (sel == 2'b01) begin
            out = c;
        end
        else begin
            out = d;
        end
    end
endmodule

// test
module test;
    reg [15:0] a, b, c, d;
    reg [1:0] sel;
    wire [15:0] out;
    
    // mux4way16_gate Instance0 (out, a, b, c, d, sel);
    mux4way16_behavioural Instance0 (out, a, b, c, d, sel);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        a[15:0] = 8'b11111111;
        b[15:0] = 8'b00000000;
        c[15:0] = 8'b11111111;
        d[15:0] = 8'b00000000;

        #(0) sel[0] = 0; sel[1] = 0; // out = a = 1
        #(1) sel[0] = 0; sel[1] = 1; // out = b = 0
        #(1) sel[0] = 1; sel[1] = 0; // out = c = 1
        #(1) sel[0] = 1; sel[1] = 1; // out = d = 0
    end

    initial begin
        $printtimescale;
        // Time scale of (test) is 1s / 1s
        $monitor ("%2d | a = %d | b = %d | c = %d | d = %d | sel = [%d, %d] | out = %d", $time, a[0], b[0], c[0], d[0], sel[0], sel[1], out[0]);
        // 0 | a = 1 | b = 0 | c = 1 | d = 0 | sel = [0, 0] | out = 1
        // 1 | a = 1 | b = 0 | c = 1 | d = 0 | sel = [0, 1] | out = 0
        // 2 | a = 1 | b = 0 | c = 1 | d = 0 | sel = [1, 0] | out = 1
        // 3 | a = 1 | b = 0 | c = 1 | d = 0 | sel = [1, 1] | out = 0
    end
endmodule