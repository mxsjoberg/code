/*
    DMux8way(in, sel) :
        If sel = 000 then { a = in, b = c = d = e = f = g = h = 0 } else if
           sel = 001 then { b = in, a = c = d = e = f = g = h = 0 } else if
           sel = 010 then { c = in, a = b = d = e = f = g = h = 0 } else if
           sel = 011 then { d = in, a = b = c = e = f = g = h = 0 } else if
           sel = 100 then { e = in, a = b = c = d = f = g = h = 0 } else if
           sel = 101 then { f = in, a = b = c = d = e = g = h = 0 } else if
           sel = 110 then { g = in, a = b = c = d = e = f = h = 0 } else if
           sel = 111 then { h = in, a = b = c = d = e = f = g = 0 }
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
module dmux8way_gate (output a, b, c, d, e, f, g, h, input in, input [2:0] sel);
    wire ao, bo, aoo, boo, coo, doo;

    dmux_gate Instance0 (ao, bo, in, sel[0]);

    dmux_gate Instance1 (aoo, boo, ao, sel[1]);
    dmux_gate Instance2 (coo, doo, bo, sel[1]);

    dmux_gate Instance3 (a, b, aoo, sel[2]);
    dmux_gate Instance4 (c, d, boo, sel[2]);
    dmux_gate Instance5 (e, f, coo, sel[2]);
    dmux_gate Instance6 (g, h, doo, sel[2]);
endmodule

// behavioural-level
module dmux8way_behavioural (output reg a, b, c, d, e, f, g, h, input in, input [2:0] sel);
    always @ (in or sel) begin
        a = 1'b0;
        b = 1'b0;
        c = 1'b0;
        d = 1'b0;
        e = 1'b0;
        f = 1'b0;
        g = 1'b0;
        h = 1'b0;
        // note: 3'b : 3 bit
        if (sel == 3'b000) begin
            a = in;
        end
        else if (sel == 3'b100) begin
            b = in;
        end
        else if (sel == 3'b010) begin
            c = in;
        end
        else if (sel == 3'b110) begin
            d = in;
        end
        else if (sel == 3'b001) begin
            e = in;
        end
        else if (sel == 3'b101) begin
            f = in;
        end
        else if (sel == 3'b011) begin
            g = in;
        end
        else begin
            h = in;
        end
    end
endmodule

// test
module test;
    reg [2:0] sel;
    reg in;
    wire a, b, c, d, e, f, g, h;
    
    // dmux8way_gate Instance0 (a, b, c, d, e, f, g, h, in, sel);
    dmux8way_behavioural Instance0 (a, b, c, d, e, f, g, h, in, sel);

    // note: #(n) : delay by n timestep (check time scale with $printtimescale)
    initial begin
        #(0) in = 1; sel[0] = 0; sel[1] = 0; sel[2] = 0; // { a = 1, b = c = d = e = f = g = h = 0 }
        #(1) in = 1; sel[0] = 0; sel[1] = 0; sel[2] = 1; // { b = 1, a = c = d = e = f = g = h = 0 }
        #(1) in = 1; sel[0] = 0; sel[1] = 1; sel[2] = 0; // { c = 1, a = b = d = e = f = g = h = 0 }
        #(1) in = 1; sel[0] = 0; sel[1] = 1; sel[2] = 1; // { d = 1, a = b = c = e = f = g = h = 0 }
        #(1) in = 1; sel[0] = 1; sel[1] = 0; sel[2] = 0; // { e = 1, a = b = c = d = f = g = h = 0 }
        #(1) in = 1; sel[0] = 1; sel[1] = 0; sel[2] = 1; // { f = 1, a = b = c = d = e = g = h = 0 }
        #(1) in = 1; sel[0] = 1; sel[1] = 1; sel[2] = 0; // { g = 1, a = b = c = d = e = f = h = 0 }
        #(1) in = 1; sel[0] = 1; sel[1] = 1; sel[2] = 1; // { h = 1, a = b = c = d = e = f = g = 0 }
    end

    initial begin
        $printtimescale;
        // Time scale of (test) is 1s / 1s
        $monitor ("%1d | in = %d | sel = [%d, %d, %d] | a = %d | b = %d | c = %d | d = %d | e = %d | f = %d | g = %d | h = %d", $time, in, sel[0], sel[1], sel[2], a, b, c, d, e, f, g, h);
        // 0 | in = 1 | sel = [0, 0, 0] | a = 1 | b = 0 | c = 0 | d = 0 | e = 0 | f = 0 | g = 0 | h = 0
        // 1 | in = 1 | sel = [0, 0, 1] | a = 0 | b = 1 | c = 0 | d = 0 | e = 0 | f = 0 | g = 0 | h = 0
        // 2 | in = 1 | sel = [0, 1, 0] | a = 0 | b = 0 | c = 1 | d = 0 | e = 0 | f = 0 | g = 0 | h = 0
        // 3 | in = 1 | sel = [0, 1, 1] | a = 0 | b = 0 | c = 0 | d = 1 | e = 0 | f = 0 | g = 0 | h = 0
        // 4 | in = 1 | sel = [1, 0, 0] | a = 0 | b = 0 | c = 0 | d = 0 | e = 1 | f = 0 | g = 0 | h = 0
        // 5 | in = 1 | sel = [1, 0, 1] | a = 0 | b = 0 | c = 0 | d = 0 | e = 0 | f = 1 | g = 0 | h = 0
        // 6 | in = 1 | sel = [1, 1, 0] | a = 0 | b = 0 | c = 0 | d = 0 | e = 0 | f = 0 | g = 1 | h = 0
        // 7 | in = 1 | sel = [1, 1, 1] | a = 0 | b = 0 | c = 0 | d = 0 | e = 0 | f = 0 | g = 0 | h = 1
    end
endmodule