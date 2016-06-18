items = []
i = 0
while 1:
    i += 1
    item = input("Enter item %d: " % i)
    if item == "":
        break
    items.append(item)
print(items)


a = ["foo", "melon"]
b = [True, False]
c = list(itertools.sum(a,b))