from pprint import pprint 

left = []
right = []
similarity = []
with open('adventofcode_1.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        left_right = line.strip('\n\r').split()
        left.append(int(left_right[0]))
        right.append(int(left_right[1]))

    pprint(left)      
    pprint(right)

    for index, l in enumerate(left):
        appearances = list(filter(lambda r: r == l, right))
        similarity.append(l * len(appearances))

    pprint(sum(similarity))