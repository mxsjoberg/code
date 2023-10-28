/*
    Mux16(a, b, sel) : If sel = 0 then for i = 0..15 out[i] = a[i] else for i = 0..15 out[i] = b[i]
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

// gate-level
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