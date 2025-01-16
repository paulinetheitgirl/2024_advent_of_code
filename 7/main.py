from copy import deepcopy

calibration = 0

def recursive_tree(running_total, factors, reversed_ops, all_reversed_ops):
    if len(factors) < 3:
        if (running_total - factors[1] == factors[0]):
            ops_copy = reversed_ops + '+'
            all_reversed_ops.append(ops_copy)
        if (running_total / factors[1] == factors[0]):
            ops_copy = reversed_ops + '*'
            all_reversed_ops.append(ops_copy)

        if len(all_reversed_ops) < 1: print(int(running_total), factors, reversed_ops, all_reversed_ops)
    else:
        diff = running_total - factors[-1]
        if (isinstance(diff, int) and diff > 0):
            ops_copy = reversed_ops + '+'
            recursive_tree(int(diff), deepcopy(factors)[:-1], ops_copy, all_reversed_ops)
        
        quot = running_total / factors[-1]
        modulo = running_total % factors[-1]
        if ((modulo == 0) and quot > 0):
            ops_copy = reversed_ops + '*'
            recursive_tree(int(quot), deepcopy(factors)[:-1], ops_copy, all_reversed_ops)

# 209536045885
# 850435817339
with open('adventofcode_7.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        all_strings = line.split(' ')
        all_numbers = [int(s.replace(':', '')) for s in all_strings]
        total_operands = len(all_numbers[1:]) - 1
        all_reversed_ops = []
        print(all_numbers[0])
        recursive_tree(all_numbers[0], all_numbers[1:], '', all_reversed_ops)
        if any(len(ops) == total_operands for ops in all_reversed_ops):
            calibration += all_numbers[0]

print('answer ', calibration)