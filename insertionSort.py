input = [2,5,3,7,4,6,1] 
inputLength = len(input)
for i in range(1,inputLength):
    current = input[i]
    for j in reversed(range(i)):
        if current < input[j]:
            input[j+1] = input[j]
            if j == 0:
                input[0] = current
        else:
            input[j+1] = current
            break
print(input)

