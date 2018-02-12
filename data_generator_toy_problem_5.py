import random

file = open("data/toy_problem_5_train.txt", "w")

sequence_length = 20

for i in range(1000):
    label = random.randint(0,sequence_length)
    x = [0] * 20
    for i in range(label):
        position = random.randint(0, sequence_length-1)
        while position < sequence_length-1 and x[position] == 1:
            position += 1
        x[position] = 1
    label = sum(x)
    x = [str(item) for item in x ]
    x = " ".join(x)
    file.write(str(label)+"\t"+str(x)+"\n")

file.flush()
file.close()