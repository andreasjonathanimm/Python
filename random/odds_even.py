n = int(input("How many numbers : "))
nums = []
odds = []
even = []
for i in range(n):
    nums.append(int(input("Enter the numbers: ")))
odds = sorted([x for x in nums if x % 2 != 0])
even = sorted([x for x in nums if x % 2 == 0])
print(f"Odds : {odds}")
print(f"Even : {even}")