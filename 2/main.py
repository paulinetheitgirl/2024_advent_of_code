from pprint import pprint 

row_count = 0
report_evals = []

def is_safe(tuple_row):
    total_flags = sum(elem[1] for elem in tuple_row)
    flag_limits = [0, len(tuple_row)]
    if total_flags not in flag_limits:
        return False
    outside_limits = list(filter(lambda elem: elem[2] < 1 or elem[2] > 3, tuple_row))
    if len(outside_limits) > 0:
        return False
    
    return True

with open('adventofcode_2.txt', mode='r', encoding='utf-8') as f:
    for index_y, line in enumerate(f):
        row_count = index_y + 1
        line = line.strip('\n\r')
        all_strings = line.split(' ')
        report_results = []
        loop_stop = len(all_strings) - 1
        for index_x, num_str in enumerate(all_strings):
            if index_x < loop_stop:
                diff = int(all_strings[index_x]) - int(all_strings[index_x + 1])
                is_pos = 1 if diff > 0 else 0
                report_results.append((diff, is_pos, abs(diff)))
        report_evals.append(report_results)
        
    # pprint(report_evals)

count = sum(1 for r in report_evals if is_safe(r))
print(count)
            