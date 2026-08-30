# 1. First practise program
'''f = open("practise.txt", "w")
f.write("Hi everyone\nWe are learning file I/o\nusing Java.\nI like programming in Java.")
f.close()'''

# 2. Second practise program
'''replace the above file data Java with Python
with open("practise.txt","r") as f:
    data = f.read()
    print("Before Replacement data is :",data)
new_data = data.replace("Java","Python")
print("After Replacement data is :",new_data)
 with open("practise.txt","w") as f:
     f.write(new_data)'''
# 3. Third program
'''def check_data(data1):
    with open("practise.txt","r") as f:
        data = f.read()
    if(data.find(data1) != -1):
        print("Found")
    else:
        print("Not Found")
check_data("xlearning")'''

# Fourth Program
'''def check_for_line(word):
    data = True
    line = 1
    with open("practise.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line)
                return
            line += 1
    
    return -1
check_for_line("Python")'''
# Fifth Program
count=0
with open("practise.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)

    
