/*
    DMux(in, sel) : If sel = 0 then { a = in, b = 0 } else { a = 0, b = in }
*/

// gate-level
module dmux_gate (output a, b, input in, sel);
    // wire : internal pin
    wire w1;
    wire w2;
    wire notsel;
    // operations
    not(notsel, sel);
    and(a, in, notsel);
    and(b, in, sel);
endmodule

// behavioural-level
module dmux_behavioural (output reg a, b, input in, sel);
    always @ (in or sel) begin
        // note: 1'b : 1 bit
        if (sel == 1'b0) begin
            a = in;
            b = 1'b0;
        end
        else begin
            a = 1'b0;
            b = in;
        end
    end
endmodule

// test
module test;
    reg in, sel;
    wire a, b;
    
    // dmux_gate Instance0 (a, b, in, sel);
    dmux_behavioural Instance0 (a, b, in, sel);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) in = 0; sel = 0; // 0, 0
        #(1) in = 1; sel = 0; // 1, 0
        #(1) in = 0; sel = 1; // 0, 0
        #(1) in = 1; sel = 1; // 0, 1
    end

    initial begin
        $printtimescale;
        // Time scale of (test) is 1s / 1s
        $monitor ("%1d | in = %d | sel = %d | a = %d | b = %d", $time, in, sel, a, b);
        // 0 | in = 0 | sel = 0 | a = 0 | b = 0
        // 1 | in = 1 | sel = 0 | a = 1 | b = 0
        // 2 | in = 0 | sel = 1 | a = 0 | b = 0
        // 3 | in = 1 | sel = 1 | a = 0 | b = 1
    end
endmodule