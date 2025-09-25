def main():
    inputs = inputData()
    average = avg(inputs[0], inputs[1])
    outputData(average)

def inputData():
    in1 = float(input("Number 1: "))
    in2 = float(input("Number 2: "))

    return in1, in2

def outputData(output):
    print(output)

def avg(num1, num2):
    total = num1 + num2
    avg = total/2

    return avg

main()