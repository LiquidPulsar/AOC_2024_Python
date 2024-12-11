from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    nums = [*map(int,f.read().split())]

LIM = 25

for _ in range(LIM):
    new_nums = []
    for num in nums:
        match num:
            case 0: new_nums.append(1)
            case n if not len(str(n))%2:
                s = str(n)  
                new_nums.append(int(s[:len(s)//2]))
                new_nums.append(int(s[len(s)//2:])) 
            case n:
                new_nums.append(n * 2024)
    nums = new_nums

    # print(nums, len(nums))
print(len(nums))
