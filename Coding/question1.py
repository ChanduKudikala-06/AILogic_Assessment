#n=5
#Input [3,4,5,1,2]
#Output:1



n=int(input("Enter length of elements:"))
numbers=[]
for i in range(n):
    value=int(input(f"Enter element {i+1}:"))
    numbers.append(value)
numbers.sort()
print(numbers[0])