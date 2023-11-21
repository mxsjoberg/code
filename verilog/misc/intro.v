/*
    http://www.techep.csi.cuny.edu/~zhangs/v.html
    iverilog -o intro intro.v; vvp intro
*/

// module < filename > (< ports >)
module intro;
    initial 
    begin
        // $display : only useful for debugging
        $display("hello verilog");
        $finish;
    end
endmodule