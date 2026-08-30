# list = [5,63,98,205,1,0,3,4,2,'apple','banana']
# list.sort()
# print(list)



# WAP to take 3 favorite movies name from user and store in a list.
# 1st method
'''movies = []
for i in range(3):
    movie = input("Enter the movie name: ")
    movies.append(movie)
print("Your favorite movies are:")
print(movies)'''

#2nd metohd

'''movies = []
movies.append(input("Enter the first movie name: "))
movies.append(input("Enter the second movie name: "))
movies.append(input("Enter the third movie name: "))
print("Your favorite movies are:")
print(movies)'''



# WAP to check if a list contains palindrome of elements or not.
list = []
for i in range(5):
    list.append(input("Enter the element: "))
palindrome = list.copy()
palindrome.reverse()
if list == palindrome:
    print("The list contains palindrome of elements.")
else:    print("The list does not contain palindrome of elements.")