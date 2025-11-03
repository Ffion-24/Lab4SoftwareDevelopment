#Creating Lists
fruits=["apple", "bannana", "cherry"]
numbers=[10,20,30,40]
mixed=["text",3.14,True]
#Access and Inexing
print(fruits[0])   #result = apple
print(fruits[-1])  #result = cherry
#Slicing
print(numbers[1:3]) #result = 20,30
print(numbers[:2])  #result = 10,20
print(numbers[-2:]) #result = 30,40
#Chaging and updateing lists
fruits[1] = "orange" # replaceing bannana with orange
print(fruits)