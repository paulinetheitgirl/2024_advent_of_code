from pprint import pprint 
import re

def mul(exp_str):
    exp_matches = re.search(r"(\d+),(\d+)", exp_str)
    return int(exp_matches.group(1)) * int(exp_matches.group(2))

# test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
with open('adventofcode_3.txt', mode='r', encoding='utf-8') as f:
    joined_lines = " ".join(f.read().splitlines())
    print(joined_lines)
    results = re.findall(r"(mul\(\d+,\d+\))", joined_lines)
            
    print(sum([*map(mul, results)]))