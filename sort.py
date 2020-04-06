order = []

    Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    order.append(value)
    sort.order()

print("Element After Sorting List in Ascending Order is : ", order)
