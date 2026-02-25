# import random 
# list1 = [1,2,3,4,5,6,7,8,9,120]
# a = random.choice(list1)
# print(a)


# random_number = random.randint(1,100)
# print("guess the number between 1 to 100")
# guess = 0


# while guess != random_number:

#     guess = int(input("Your guess: "))

#     if guess == random_number:
#         break;
#     elif guess < random_number:
#         print("print Higher number!")
        
#     elif guess > random_number:
#         print("print Lower number!")
    

# print("You got the number!") 
# if (guess == 5):
#     print("your time is up")





import random

num = random.randint(0, 100)
a = int(input("Enter a number: "))
v = 0

if num == a:
    print("It's a correct number.")
else:
    for v in range(5):
        if num > a:
            a = int(input("Your number is smaller: "))
        elif num < a:
            a = int(input("Your number is greater: "))
        else:
            print("It's a correct number.")
            break
    else:
        print("Your time is up")




    




