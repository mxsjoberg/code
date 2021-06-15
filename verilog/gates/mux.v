/*
    Mux(a, b, sel) : If sel = 0 then out = a else out = b
*/

// gate-level
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

// behavioural-level
module mux_behavioural (output reg out, input a, b, sel);
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
    reg a, b, sel;
    wire out;
    
    // mux_gate Instance0 (out, a, b, sel);
    mux_behavioural Instance0 (out, a, b, sel);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) a = 0; b = 0; sel = 0; // 0
        #(1) a = 0; b = 1; sel = 0; // 0
        #(1) a = 1; b = 0; sel = 0; // 1
        #(1) a = 1; b = 1; sel = 0; // 1
        #(1) a = 0; b = 0; sel = 1; // 0
        #(1) a = 0; b = 1; sel = 1; // 1
        #(1) a = 1; b = 0; sel = 1; // 0
        #(1) a = 1; b = 1; sel = 1; // 1
    end

    initial begin
        $printtimescale;
        // Time scale of (test) is 1s / 1s
        $monitor ("%1d | a = %d | b = %d | sel = %d | out = %d", $time, a, b, sel, out);
        // 0 | a = 0 | b = 0 | sel = 0 | out = 0
        // 1 | a = 0 | b = 1 | sel = 0 | out = 0
        // 2 | a = 1 | b = 0 | sel = 0 | out = 1
        // 3 | a = 1 | b = 1 | sel = 0 | out = 1
        // 4 | a = 0 | b = 0 | sel = 1 | out = 0
        // 5 | a = 0 | b = 1 | sel = 1 | out = 1
        // 6 | a = 1 | b = 0 | sel = 1 | out = 0
        // 7 | a = 1 | b = 1 | sel = 1 | out = 1
    end
endmodule