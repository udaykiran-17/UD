import random
import time

Operators =["+", "-", "*"]
input("click enter to enter Min & Max values")
Min_value = int(input("Min value :"))
Max_value = int(input("Max value :"))
Total_problems = int(input("total problems you need :"))


def generate_problem():
    left = random.randint(Min_value,Max_value)
    rigth = random.randint(Min_value,Max_value)
    operator =random.choice(Operators)

    exp = str(left) + " " + operator + " " + str(rigth)
    answer = eval(exp)
    return exp,answer


incorrect = 0
input("press ENTER to start ")
print("**********************")

start_time = time.time()

for i in range(Total_problems):
    exp, answer = generate_problem()
    while True:
        Guess = input("Problem #" + str(i+1) + " : " + exp + " = ")
        if Guess == str(answer):
            break
        incorrect +=1

end_time = time.time()
total_time = round(end_time - start_time,2)

print("**********************")
print("NO.OF INCCORECT ANSWERS : ",incorrect)
print("**********************")
print("GOOD JOB! You completed in", total_time, "seconds")