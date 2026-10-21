import time
numbers = (2,7,4,"phone","allwar","damm","oppo",1,3,5,9,2,0)
time.sleep(0.3)
print(type(numbers))

#packing - The process of assigning values to a tuple is known as packing

address = ("308","Negra Arroyo Lane","Albuquerque","New Mexico","87104")
time.sleep(0.3)
print(address)
time.sleep(0.3)
for i in address:
    print(i)
    time.sleep(0.3)


# unpacking - Unpacking tuples assigns the objects in a tuple to multiple variables

houseno,apartment,city,state,pin = address

print("house number :",houseno)
time.sleep(0.3)
print("street :" ,apartment)
time.sleep(0.3)
print("city :" ,city)
time.sleep(0.3)
print("state :" ,state)
time.sleep(0.3)
print("post address :" ,pin)
time.sleep(0.3)

desktop = "firefox","zoom.us","finder"

print(type(desktop))
time.sleep(0.3)
print(desktop[0])

#Nested tuple

myTuple = ("mouse", (1,2,3),[10,45,60])
print(myTuple[1][0])
time.sleep(0.3)
print(myTuple[0][3])
time.sleep(0.3)
#tuple immutable - you cannot change value of tuple
#              myTuple[0][3] = "v"

#Concatenation
my_taple1 = ("green", "yellow")
my_taple2 = ("red", "blue")
my_taple3 = my_taple1 + my_taple2
time.sleep(0.3)
print(my_taple3)
time.sleep(0.3)
print(len(my_taple3))
time.sleep(0.3)
print(my_taple3 * 3)
time.sleep(0.3)
food = ("Osama burger","Obama value meal","burger king jr meal")
if "sad meal" in food:
    print("bro stop being emo")
    time.sleep(0.3)
else:
    print("Get a chance!")
    time.sleep(0.3)

#slicing operater
tupler = ("B","A","L","L","I","N")

print(tupler[0:3])
time.sleep(0.3)
print(tupler[:3])
time.sleep(0.3)
print(tupler[3:6])
time.sleep(0.3)
print(tupler[3:])