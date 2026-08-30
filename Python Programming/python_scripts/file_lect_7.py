# 1. for writing we use w
# f = open("demo.txt","w")
# f.write("Hello,this is python file demo")
# f.close()
# 2. for overrite we use r+
# f = open("demo.txt","r+")
# f.write("Nextline")
# data = f.read()
# print(data)
# f.close()
# 3. for read and append we use a+
# f = open("demo.txt","a+")
# f.write("good coding")
# data = f.read()
# print(data)
# f.close()
# 4. for read the data we use r
# f = open("demo.txt","r")
# print(f.read())
# f.close()
# 5. with syntax we can avoid close the file
# with open("demo.txt","r") as f:
#     demo = f.read()
#     print(demo)
# with open("demo.txt","w") as f:
#     f.write("this is the further other work")
# with open("demo.txt","a") as f:
#     f.write("hello this is the other work")
# 6. Removal of file
# import os
# os.remove("sample.txt")