import math
import random


def task_generator(low_limit, up_limit):

    operation_list = ['+', '*', '-']
    number_1 = random.randint(low_limit, up_limit)
    number_2 = random.randint(low_limit, up_limit)
    sign = random.choice(operation_list)
    operation = " ".join([str(number_1), sign, str(number_2)])

    return operation, sign, number_1, number_2


def result_task(x, y, oper):

    if oper == '+':
        return x + y
    if oper == '-':
        return x - y
    if oper == '*':
        return x * y


task_counter = 1
grade = 0
level = ""
level_description = ""

while True:

    print("Which level do you want? Enter a number:\n"
          "1 - simple operations with numbers 2-9\n"
          "2 - integral squares 11-29")

    difficulty = input()

    if difficulty == "1":

        level = 1
        level_description = "simple operations with numbers 2-9"

        while task_counter < 6:

            task, operator, A, B = task_generator(2, 9)

            print("Task to solve: ", task)

            result = result_task(A, B, operator)

            while True:

                try:

                    user_answer = int(input("Enter your answer: "))

                    if user_answer == result:
                        print("Right!")
                        grade += 1
                        break
                    else:
                        print("Wrong!")
                        break

                except ValueError or None:

                    print("Incorrect format.")

            task_counter += 1

        break

    elif difficulty == '2':

        level = 2
        level_description = "integral squares 11-29"

        while task_counter < 6:

            number = random.randint(11, 29)

            square_number = math.pow(number, 2)

            print(f'What is the integral square of {number}?')

            while True:

                try:

                    answer = int(input("Enter your answer: "))

                    if answer == square_number:
                        print("Right!")
                        grade += 1
                        break
                    else:
                        print("Wrong!")
                        break

                except ValueError or None:

                    print("Incorrect format.")

            task_counter += 1

        break

    else:
        print('Incorrect format.')

print(f'Your mark is {grade}/5.')

print("Would you like to save your result to the file? Enter yes or no.")

save_decision = input()

choices = ["YES", "yes", "Yes", "y"]

if save_decision in choices:

    username = input("What is your name?\n")

    file = open(f'{username}.txt', 'w', encoding='utf-8')

    file.write(f'{username}: {grade}/5 in level {level} ({level_description})')

    file.close()

    print(f"The results are saved in {file.name}.")

else:
    exit(0)
