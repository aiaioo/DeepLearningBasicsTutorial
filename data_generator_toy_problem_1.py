import random

file = open("data/toy_problem_1_test.txt", "w")

for i in range(1000):
    y = random.randint(-100,100)
    x = random.randint(-100,100)
    if x == y:
        y += 1
    label = 0 if y < x else 1
    file.write(str(label)+"\t"+str(x)+" "+str(y)+"\n")

file.flush()
file.close()