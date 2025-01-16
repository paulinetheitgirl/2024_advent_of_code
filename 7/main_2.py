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
        if running_total == int(str(factors[0]) + str(factors[1])):
            ops_copy = reversed_ops + '|'
            all_reversed_ops.append(ops_copy)

        # print(int(running_total), factors, reversed_ops, all_reversed_ops)
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
        
        # we know there are at least 3 factors
        concat_val = int(str(factors[-2]) + str(factors[-1]))
        ops_copy = reversed_ops + '|'
        recursive_tree(running_total, deepcopy(factors)[:-2] + [concat_val], ops_copy, all_reversed_ops)

        diff_concat_val = int(str(factors[-3] + factors[-2]) + str(factors[-1]))
        diff = running_total - diff_concat_val
        if (isinstance(diff, int) and diff > 0):
            ops_copy = reversed_ops + '+'
            recursive_tree(int(running_total), deepcopy(factors)[:-3] + [factors[-3] + factors[-2], factors[-1]], ops_copy, all_reversed_ops)
        
        quot_concat_val = int(str(factors[-3] * factors[-2]) + str(factors[-1]))
        quot = running_total / quot_concat_val
        modulo = running_total % quot_concat_val
        if ((modulo == 0) and quot > 0):
            ops_copy = reversed_ops + '*'
            recursive_tree(int(running_total), deepcopy(factors)[:-3] + [factors[-3] * factors[-2], factors[-1]], ops_copy, all_reversed_ops)   

with open('adventofcode_7.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        all_strings = line.split(' ')
        all_numbers = [int(s.replace(':', '')) for s in all_strings]
        total_operands = len(all_numbers[1:]) - 1
        all_reversed_ops = []
        recursive_tree(all_numbers[0], all_numbers[1:], '', all_reversed_ops)
        print(all_numbers[0], all_reversed_ops)
        if any(len(ops) == total_operands for ops in all_reversed_ops):
            calibration += all_numbers[0]

print('answer ', calibration)