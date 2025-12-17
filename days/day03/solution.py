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

def get_max_joltage(s, amount) -> int:
    result = ''
    for skip in range(amount - 1, -1, -1):
        # Finds the index of the maximum digit in s up to len(s) - skip
        idx = max(range(len(s) - skip), key=lambda i: s[i])
        # Append the found maximum digit to the result and update s to the remaining substring
        result, s = result + s[idx], s[idx + 1:]
    return int(result)

def part1(data: str) -> int:
    lines = data.strip().split('\n')
    result = 0
    for line in lines:
        result += get_max_joltage(line, 2)

    return result

def part2(data: str) -> int:
    lines = data.strip().split('\n')
    result = 0
    for line in lines:
        result += get_max_joltage(line, 12)

    return result
