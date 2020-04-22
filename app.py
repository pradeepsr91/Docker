num = int(input("Enter a number"))
divisor = range(2, 15)

outputList = []
for numbers in divisor:
    if (num % numbers) == 0:
        outputList.append(numbers)
print(outputList)
