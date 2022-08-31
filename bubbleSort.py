input = [2,5,3,7,4,6,1] 
inputLength = len(input)
for i in range(inputLength, 0 , -1):
    for j in range(i):
        if j < inputLength-1:
            if input[j] > input[j+1]:
                temp = input[j+1]
                input[j+1] = input[j]
                input[j] = temp
print(input)
