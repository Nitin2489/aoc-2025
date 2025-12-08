'''
Input: Each line of digits in input corresponds to a single bank of batteries

We need to turn on exactly 2 batteries within a bank of batteries.

Need to find the largest possible joltage each bank can produce (note: you can NOT rearrange batteries)

examples:
987654321111111 -> largest possible is 98
811111111111119 -> 89 is largest
234234234234278 -> 78 is the largest
818181911112111 -> 92 is the largest

return sum of the maximum joltage from each bank
'''

def part1(data: str) -> int:
    lines = data.strip().split('\n')
    for line in lines:
        print(line)
    return 0

def part2(data: str) -> int:
    lines = data.strip().split('\n')
    # Your solution here
    return 0
