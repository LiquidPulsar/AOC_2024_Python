from pathlib import Path
from collections import Counter

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    nums = Counter(map(int,f.read().split()))

LIM = 75

# lens[i] = len(nums) after i iterations

for _ in range(LIM):
    new_nums = Counter()
    for num,count in nums.items():
        match num:
            case 0: new_nums[1] += count
            case n if not len(str(n))%2:
                s = str(n)  
                new_nums[int(s[:len(s)//2])] += count
                new_nums[int(s[len(s)//2:])] += count
            case n:
                new_nums[n * 2024] += count
    nums = new_nums
print(sum(nums.values()))
