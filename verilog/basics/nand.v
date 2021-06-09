// gate-level
module _nand (output Y, input A, B);
    // wire is electrical connection
    wire Yd;
    
    // operations (gate-level)
    and(Yd, A, B);                  // Yd = 1 if A = 1 and B = 1, else Yd = 0
    not(Y, Yd);                     // Y = 0 if Yd = 1, else Y = 1
endmodule

// behavioural modeling
module _nand_model (output reg Y, input A, B);
    always @ (A or B) begin
        if (A == 1'b1 & B == 1'b1) begin
            Y = 1'b0;
        end
        else begin
            Y = 1'b1;
        end
    end
endmodule

// test
module _nand_test;
    reg A, B;
    wire Y;
    
    // _nand Instance0 (Y, A, B);
    _nand_model Instance0 (Y, A, B);

    initial begin
        #(0) A = 0; B = 0;
        #(1) A = 0; B = 1;          // delay by one timestep
        #(1) A = 1; B = 0;          // delay by one timestep
        #(1) A = 1; B = 1;          // delay by one timestep
    end

    initial begin
        $printtimescale;
        // Time scale of (_nand_test) is 1s / 1s
        
        $monitor ("%t | A = %d| B = %d| Y = %d", $time, A, B, Y);
        // 0 | A = 0| B = 0| Y = 1
        // 1 | A = 0| B = 1| Y = 1
        // 2 | A = 1| B = 0| Y = 1
        // 3 | A = 1| B = 1| Y = 0
    end
endmodule