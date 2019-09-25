#Shawntal 

# Create a program that can randomly generate a series of math problems that can be 
# imported into a Learning Management System (LMS) for the purpose of creating online math tests. 
# The goal is to reduce the manual effort required to create these online math tests
# by having a program generate the test questions, 
# along with varying the questions and answers, instead of a human having to do this task by hand.

import random

number_of_questions = int(input("How many questions would you like to generate?: \n"))


for i in range(number_of_questions):
    num1_num = random.choice(range(99))
    num2_num = random.choice(range(99))
    print(f"\nWhat is {num1_num} + {num2_num}\n")
else:
    print("\n Completion of Questions")
    
for i in range(number_of_questions):
    num1_num = random.choice(range(99))
    num2_num = random.choice(range(99))
    print(f"\nWhat is {num1_num} - {num2_num}\n")
else:
    print("\n Completion of Questions")
    
for i in range(number_of_questions):
    num1_num = random.choice(range(99))
    num2_num = random.choice(range(99))
    print(f"\nWhat is {num1_num} * {num2_num}\n")
else:
    print("\n Completion of Questions")
    
for i in range(number_of_questions):
    num1_num = random.choice(range(99))
    num2_num = random.choice(range(99))
    print(f"\nWhat is {num1_num} / {num2_num}\n")
else:
    print("\n Completion of Questions")
