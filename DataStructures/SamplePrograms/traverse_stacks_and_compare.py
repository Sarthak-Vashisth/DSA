def traverse_while_compare(list1, element):
    while list1 and element > list1[-1]:
        list1.pop()
    #list1.append(element)
    print(list1)


traverse_while_compare([2,6,4], 5)
