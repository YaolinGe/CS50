import random


while True: 
    try:
        n = int(input("Level: ").strip())
        if n > 0:
            break
    except ValueError:
        continue

number = random.randint(1, n)
while True:
    num = input("Guess: ").strip()
    try:
        num = int(num)
        if num > 0:
            if num == number:
                print("Just right!")
                break
            elif num > number:
                print("Too large!")
            elif num < number:
                print("Too small!")
    except ValueError:
        continue
    


# level = int(level)
# answer = random.randrange(0, level)

# while True:
#     guess = input('Guess: ')
#     try:
#         if int(guess) >0 and int(guess) <= level:
#             guess = int(guess)
            
#             if guess == answer:
#                 print('Just right!')
#                 break
#             elif guess > answer:
#                 print('Too large!')
#             elif guess < answer:
#                 print('Too small!')
#     except ValueError:
#         continue