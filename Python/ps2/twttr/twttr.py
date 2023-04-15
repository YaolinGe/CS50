vowels = ['a', 'e', 'i', 'o', 'u']
user_input = input("Input: ").strip()
print("Output: ", end="")
for char in user_input:
    if char.lower() not in vowels:
        print(char, end="")
print("")

# submit50 cs50/problems/2022/python/twttr