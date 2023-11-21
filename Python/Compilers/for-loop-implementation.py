import timeit

def not_for_loop(index = 0, elements = [], operation = None):
    if index < len(elements):
        if operation is not None:
            elements[index] = operation(elements[index])

        not_for_loop(index + 1, elements, operation)

    return elements

def for_loop_using_while(elements = [], operation = None):
    index = 0
    while index < len(elements):
        if operation is not None:
            elements[index] = operation(elements[index])
        index += 1

    return elements

def for_loop(elements = [], operation = None):
    for index in range(len(elements)):
        elements[index] = operation(elements[index])

    return elements

# print(not_for_loop(0, [1, 2, 3, 4, 5], lambda x: x.__add__(1)))
# print(for_loop_using_while([1, 2, 3, 4, 5], lambda x: x.__add__(1)))
# print(for_loop([1, 2, 3, 4, 5], lambda x: x.__add__(1)))

assert not_for_loop(0, [1, 2, 3, 4, 5], lambda x: x.__add__(1)) == [2, 3, 4, 5, 6]
assert for_loop_using_while([1, 2, 3, 4, 5], lambda x: x.__add__(1)) == [2, 3, 4, 5, 6]
assert for_loop([1, 2, 3, 4, 5], lambda x: x.__add__(1)) == [2, 3, 4, 5, 6]

print(timeit.timeit('not_for_loop(0, [1, 2, 3, 4, 5], lambda x: x.__add__(1))', setup = 'from __main__ import not_for_loop', number = 100000))
# 0.10954952286556363
print(timeit.timeit('for_loop_using_while([1, 2, 3, 4, 5], lambda x: x.__add__(1))', setup = 'from __main__ import for_loop_using_while', number = 100000))
# 0.08992556994780898
print(timeit.timeit('for_loop([1, 2, 3, 4, 5], lambda x: x.__add__(1))', setup = 'from __main__ import for_loop', number = 100000))
# 0.08654258819296956