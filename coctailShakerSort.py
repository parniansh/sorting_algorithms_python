input = [2,5,3,7,4,6,1] 
inputLength = len(input)
for i in range(0, inputLength):
    minNumber = input[i]
    minIndex = i

    for j in range(i,inputLength):

        if input[j] < minNumber:
            minNumber = input[j]
            minIndex = j
    input[minIndex] = input[i]
    input[i] = minNumber
    
    
print(input)

