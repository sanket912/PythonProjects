#return max from 3 numbers

num1 = int(input("Enter 1: "))
num2 = int(input("Enter 2: "))
num3 = int(input("Enter3: "))
lst = [num1, num2, num3]
def max_num(a):
    lt = [i for i in a]
    lt = set(lt)
    lt = list(lt)
    print(lt[-1])

print(max_num(lst))