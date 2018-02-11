import random

file = open("data/toy_problem_2_train.txt", "w")

for i in range(1000):
    y = random.randint(-100,100)
    z = random.randint(-100,100)
    x = y + z
    label = random.randint(0,1)
    if label == 0:  # y + z < x
        x += random.randint(1,100)
    else:  # y + z > x
        x -= random.randint(1,100)
    file.write(str(label)+"\t"+str(x)+" "+str(y)+" "+str(z)+"\n")

file.flush()
file.close()