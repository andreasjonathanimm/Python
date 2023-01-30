# 1) Iterate with enumerate() instead of range(len())
data = [1, 2, -4, -3]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0
print(data)

# 2) Use List Comprehensions instead of raw loops
squares = [i*i for i in range(10)]
print(squares)

# 3) Sort complex iterables with sorted()
data = (3, 5, 1, 10, 9)
sorted_data = sorted(data, reverse=True)
print(sorted_data)

data = [{"name": "Max", "age": 6}, {"name": "Lisa", "age": 20}, {"name": "Ben", "age": 9}]
sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)

# 4) Store unique values with Sets
my_list = [1,2,3,4,5,6,7,7,7,7]
my_set = set(my_list)
print(my_set)

primes = {2,3,5,7,11,13,17,19}
print(primes)

# 5) Save Memory with Generators
import sys
my_gen = (i for i in range(10000))
print(sum(my_gen))
print(sys.getsizeof(my_gen), "bytes")

# 6) Define default values in Dictionaries with .get() and .setDefault()
my_dict = {"item": "football", "price": 10.00}
count = my_dict.get("count", 0)
print(count)

count = my_dict.setdefault("count", 0)
print(count)
print(my_dict)

# 7) Count hashable objects with collections.Counter
from collections import Counter
my_list = [10,10,10,5,5,2,9,9,9,9,9,9]
counter = Counter(my_list)
most_common = counter.most_common(1)
print(most_common[0][0]) #Gets the most common value

# 8) Format Strings with f-Strings (3.6+)
name = "Alex"
my_string = f"Hello {name}"
print(my_string)

i = 10
print(f"{i} squared is {i*i}")

# 9) Concatenate string with .join()
list_of_strings = ["Hello", "my", "friend"]
my_string = " ".join(list_of_strings)
print(my_string)

# 10) Merge Dictionaries with {**d1, **d2} (3.5+)
d1 = {"name": "Alex", "age": 25}
d2 = {"name":"Alex","city":"New York"}
merged_dict = {**d1, **d2}
print(merged_dict)

# 11) Simplify if-statement with if x in [a,b,c]
colors = ["red", "green","blue"]
c = "red"
if c in colors:
    print("is main color")