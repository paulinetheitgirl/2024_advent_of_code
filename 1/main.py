from pprint import pprint 

left = []
right = []
diff = []
with open('adventofcode_1.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        left_right = line.strip('\n\r').split()
        left.append(int(left_right[0]))
        right.append(int(left_right[1]))

    left.sort()
    right.sort()
    pprint(left)      
    pprint(right)

    for index, l in enumerate(left):
        diff.append(abs(l - right[index]))

    print(diff, sum(diff))