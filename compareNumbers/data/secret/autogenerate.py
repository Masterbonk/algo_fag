import random
for x in range(1,51):
    first = "file" + str(x) + ".in"
    file = open(first, "w")
    a = random.randint(0,100)
    b = random.randint(0,100)
    file.write(str(a) + "\n")
    file.write(str(b))
    file.close()
    second = "file" + str(x) + ".ans"
    answerFile = open(second, "w")
    if (a>b):
        answerFile.write("bigger")
    elif (b>a):
        answerFile.write("smaller")
    else:
        answerFile.write("equal")
    answerFile.close()
    


