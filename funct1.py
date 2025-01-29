def ounc(gr):
    print(28.34952321*gr)
def fahr(f):
    print((5/9)*(f-32))
def solve(numheads, numlegs):
    for rabbits in range(numheads + 1): 
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def filt(list):
    for x in list:
        if is_prime(x):
            print(x)
from itertools import permutations
def print_permutations(user_input):
    perm_list = permutations(user_input)
    for perm in perm_list:
        print(''.join(perm))
def reverse_words(sentence):
    reversed_sentence = ' '.join(sentence.split()[::-1])
    return reversed_sentence
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
def spy_game(nums):
    for i in range(len(nums)-1):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
import math
def vol(r):
    return (4/3)*3.1416*(r**3)
def unique_elem(lst1,lst2):
    for x in lst1:
        if lst1.count(x)==1:
            lst2.append(x)
def is_palindrome(phr):
    for x in range(len(phr)//2):
        if phr[x]!=phr[len(phr)-x-1]:
            return False
    return True
def histogram(lst):
    for x in lst:
        print("*" * x)  
import random
def guessnum():
    rand_num=random.randint(1,20)
    name=input("Hello! What is your name?")
    a=int(input(f"Well,{name}, I am thinking of a number between 1 and 20.\nTake a guess."))
    count=0
    if a>rand_num:
        a=int(input("Your guess is too high.\nTake a guess"))
        count+=1
    if a<rand_num:
        a=int(input("Your guess is too low\nTake a guess."))
        count+=1
    if a==rand_num:
        print(f"Good job,{name}! You guessed my number in {count} guesses!")
        return True
guessnum()