l = int(input())
testcase = []

for i in range(l) :
    testcase.append(input())

for i in range(l) :
    score = 0
    f = 0
    for case in testcase[i] :
        if (case == "O") :
            f += 1
            score += f
        elif (case == "X") :
            f = 0
    print(score)