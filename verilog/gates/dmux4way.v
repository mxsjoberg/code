/*
    DMux4way(in, sel) :
        If sel = 00 then { a = in, b = c = d = 0 } else if
           sel = 01 then { b = in, a = c = d = 0 } else if
           sel = 10 then { c = in, a = b = d = 0 } else if
           sel = 11 then { d = in, a = b = c = 0 }
*/

// dmux.v
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

// gate-level
module dmux4way_gate (output a, b, c, d, input in, input [1:0] sel);
    wire ao, bo;

    dmux_gate Instance0 (ao, bo, in, sel[0]);
    dmux_gate Instance1 (a, b, ao, sel[1]);
    dmux_gate Instance2 (c, d, bo, sel[1]);
endmodule

// behavioural-level
module dmux4way_behavioural (output reg a, b, c, d, input in, input [1:0] sel);
    always @ (in or sel) begin
        a = 1'b0;
        b = 1'b0;
        c = 1'b0;
        d = 1'b0;
        // note: 2'b : 2-bit
        if (sel == 2'b00) begin
            a = in;
        end
        else if (sel == 2'b10) begin
            b = in;
        end
        else if (sel == 2'b01) begin
            c = in;
        end
        else begin
            d = in;
        end
    end
endmodule

// test
module test;
    reg [1:0] sel;
    reg in;
    wire a, b, c, d;
    
    // dmux4way_gate Instance0 (a, b, c, d, in, sel);
    dmux4way_behavioural Instance0 (a, b, c, d, in, sel);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) in = 1; sel[0] = 0; sel[1] = 0; // { a = 1, b = c = d = 0 }
        #(1) in = 1; sel[0] = 0; sel[1] = 1; // { b = 1, a = c = d = 0 }
        #(1) in = 1; sel[0] = 1; sel[1] = 0; // { c = 1, a = b = d = 0 }
        #(1) in = 1; sel[0] = 1; sel[1] = 1; // { d = 1, a = b = c = 0 }
    end

    initial begin
        $printtimescale;
        // Time scale of (test) is 1s / 1s
        $monitor ("%1d | in = %d | sel = [%d, %d] | a = %d | b = %d | c = %d | d = %d", $time, in, sel[0], sel[1], a, b, c, d);
        // 0 | in = 1 | sel = [0, 0] | a = 1 | b = 0 | c = 0 | d = 0
        // 1 | in = 1 | sel = [0, 1] | a = 0 | b = 1 | c = 0 | d = 0
        // 2 | in = 1 | sel = [1, 0] | a = 0 | b = 0 | c = 1 | d = 0
        // 3 | in = 1 | sel = [1, 1] | a = 0 | b = 0 | c = 0 | d = 1
    end
endmodule