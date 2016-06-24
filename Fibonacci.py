# Fibonacci Series.

numbers = int(input("How many: "))
start = [0,1]

def Fibonacci(a):
    return start.append(start[-1] + start[-2])

for i in range(numbers-2):
    Fibonacci(start)

print(start)