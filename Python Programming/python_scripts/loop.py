# Element = [1,4,9,16,25,36,49,64,81,100]
# for val in Element:
#     print(val)
n = int(input("Enter the number: "))
sum = 0
while(n!=0):
    sum = sum+n
    n=n-1
print("Sum is: ",sum)