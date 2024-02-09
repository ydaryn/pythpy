#ex1
def grams_to_ounces(grams):
    return 28.3495231 * grams

#ex2
def faren_to_celci(farenh):
    return (farenh - 32) * 5 / 9

#ex3
def solve(numheads, numlegs):
    chickens = (numlegs - 2 * numheads) / 2
    rabbits = numheads - chickens
    return (int(rabbits), int(chickens))

#ex4
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

#ex5
from itertools import permutations
def print_permutations(string):
    perms = permutations(string)
    for perm in perms:  #print each
        print(''.join(perm))  #join is to complete all elements in one str
        
#ex6
def reverse(st):
    sentence = list(map(str, st.split( )))
    sentence.reverse()
    return sentence
        
#ex7
def cons_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] == 3:
            return True
    return False

#ex8
def spy_game(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            if 0 in nums[i+1:] and 7 in nums[i+1:]:
                return True
    return False

#ex9
def sphere_volume(radius):
    return 4/3 * 3.14 * radius**3 

#ex10
def unique(a):
    new_a = []
    for x in a:
        if x not in new_a:
            b.append(x)
    return b

#ex11
def is_palindrome(word):
    return word == word[::-1]

#ex12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

#ex13
import random
def guess_the_number():
    num = random.randint(1, 20)
    guesses_count = 0

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    while True:
        print("Take a guess.")
        guess_num = int(input())
        guesses_count += 1

        if guess_num < num:
            print("Your guess is too low.")
        elif guess_num > num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_count} guesses!")
            break
        
#ex14 ok        
