/*
    Verilog is a structured, hardware description language developed by Prabhu Goel et al in 1984.

    https://en.wikipedia.org/wiki/Verilog
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

/*
    online simulator:
        http://www.techep.csi.cuny.edu/~zhangs/v.html
    
    run from command-line:
        $ iverilog -o intro intro.v
        $ vvp intro

    build system (sublime text):
    {
        "shell": true,
        "cmd": ["iverilog -o ${file_path}/${file_base_name} ${file} && vvp ${file_path}/${file_base_name}"],
        "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
        "working_dir": "${file_path}",
    }
*/