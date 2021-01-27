list1 = []
list2 = []
n = int(input("Enter number of elements:"))

for i in range(0, n):
    element = int(input())
    list1.append(element)
print("Input:list1=",list1)

for num in list1:
    if num>=0:
        list2.append(num)
print("output:",list2)
