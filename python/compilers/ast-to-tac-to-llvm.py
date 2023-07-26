from mako.template import Template

def gen_tac(ast, tmp_counter):
    if isinstance(ast, int):
        return f"t{tmp_counter} = {ast}", f"t{tmp_counter}", tmp_counter + 1
    elif isinstance(ast, list):
        op = ast[0]
        left, left_var, tmp_counter = gen_tac(ast[1], tmp_counter)
        right, right_var, tmp_counter = gen_tac(ast[2], tmp_counter)
        tmp_var = f"t{tmp_counter}"
        result = f"{tmp_var} = {left_var} {op} {right_var}"
        return f"{left}\n{right}\n{result}", tmp_var, tmp_counter + 1
    else:
        raise Exception("unknown node")

def tac_to_llvm(tac):
    code = []
    var_map = {}

    code.append("define i32 @main(i32) {")

    for line in tac.strip().split('\n'):
        parts = line.split(' ')
        destination_var = parts[0]
        operation = parts[1]
        operands = parts[2:]

        if len(parts) == 3 and operation == '=':
            if operands and operands[0].isdigit():
                code.append(f"\t%{destination_var} = add i32 {operands[0]}, 0")
            else:
                code.append(f"\t%{destination_var} = add i32 %{var_map[operands[0]]}, 0")
            var_map[destination_var] = destination_var
        else:
            # replace assignment with operation
            operation = parts[3]
            if operands[0].isdigit():
                op1 = f"{operands[0]}"
            else:
                op1 = f"%{var_map[operands[0]]}"
            if operands[2].isdigit():
                op2 = f"{operands[2]}"
            else:
                op2 = f"%{var_map[operands[2]]}"

            if operation == '+':
                code.append(f"\t%{destination_var} = add i32 {op1}, {op2}")
            elif operation == '-':
                code.append(f"\t%{destination_var} = sub i32 {op1}, {op2}")
            elif operation == '*':
                code.append(f"\t%{destination_var} = mul i32 {op1}, {op2}")
            elif operation == '/':
                code.append(f"\t%{destination_var} = sdiv i32 {op1}, {op2}")
            else:
                raise ValueError(f"Unsupported operation: {operation}")

            var_map[destination_var] = destination_var

    code.append(f"\tret i32 %{var_map[destination_var]}")
    code.append("}")

    return '\n'.join(code)


ast = ["+", 2, ["*", 3, 4]]
tac = gen_tac(ast, 1)[0]
# t1 = 2
# t2 = 3
# t3 = 4
# t4 = t2 * t3
# t5 = t1 + t4

print(tac_to_llvm(tac))
# define i32 @main(i32) {
#     %t1 = add i32 2, 0
#     %t2 = add i32 3, 0
#     %t3 = add i32 4, 0
#     %t4 = mul i32 %t2, %t3
#     %t5 = add i32 %t1, %t4
#     ret i32 %t5
# }
