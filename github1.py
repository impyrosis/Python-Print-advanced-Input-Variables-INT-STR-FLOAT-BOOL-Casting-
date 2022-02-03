# 1. Display any 5 strings in one line using the print() command

a= "PowerBI"
b= "Tableau"
c= "Salesforce"
d = "SAP"
e = "Python"

print ("Five most popular technology softwares:" ,(a) , (b), (c), (d), (e))

# 2  2. Display any 5 integers in one line using the print() command

a= 14
b=43
c=56
d =10
e= 65

 print( int(a), int(b), int(c), int(d), int(e))

# 3. Display any 5 float numbers in one line using the print() command

a= 34
b=32
c=56
d=98
e=188
print (float(a), float(b), float(c), float(d), float(e))

# 4. Display a combination of integers and strings in one line

a= "Rao"
b = 2018
c =39
d = "netizen"
e = "pyhton"
f = 2022
g= 32
h= "but looks he is only"
print(str(a), "is such a handsome guy, he is only," ,int(c), str(h), int(g), str(a),
     "calls himself", str(d), "his favourite programming language is", str(e), str(a),
     "landed in Canada in", int(b), "but in", int(f), "he is optimisitc that he "
    "will become Canadian Citizen"
     )

# 5. Define a few variables and give an example on how to use f'' formatting strings (display strings and numeric variables)

name= "Shani"
height = 180
f'' "he said his alias is {name}"

name = 'Shani'
age = 36
height =185
nationality = "Netizen"

print( f'{name} is handsome', f'and {name} claims that his nationality is ' f'{nationality}',
'and height of', f'{name} is ' f'{height}')


# 6. Display in one print command 5 strings, 5 integers, 5 float numbers, and 2 Boolean values together

a = "Emirates Air lines"
b = "Air Bus"
c = "A"
d= "Air Bus A-380"
ton = "tons"
model = 380
weight = 620
capacity = 525
No_of_people = "passengers"
launch_yr = 1990
No_of_engines = 4
water_draw = 2.5
Maintain = 7.4
Avg_seat_width = 44.5
wingspan = 79.8

print (f'{a}, is the biggest airline in the world who also owns', f'{b} {c} {model}. '
      , f'it is interesting to note that {d} has weight of {weight} {ton} and capacity of {capacity} {No_of_people}'
      f' and it was launched in {launch_yr}. it has water draw of {water_draw}{ton}. '
        f'It maintains distance of {Maintain} Km with other {d}. The average seat width is {Avg_seat_width} cm. '
        f'Average wingspan is {wingspan} cm. {d} has {No_of_engines} number of engines.')

if capacity==525:
   print ("Passenger Capacity of Air Bus A 380 is True")


# 7. Combine print and input together in one line


a= input("Please Enter Your Nationality:")
print("Nice to meet you", (a) )


# 8. Provide multiple inputs in one go

a = input(" Enter your First Name: ")
b = input("Enter your Last Name: ")
c = input("If you are 18 years above then Enter your age: ")
d = input("Enter your City: ")
print("Welcome to Online Mart :", (a), (b))

# 9. Reversing a string in Python

a= "Amazon is the biggest online ecommerce on this planet" [::-1]
print(a)

# 10. In-Place Swapping Of Two Numbers


a= input("Enter the First number of your choice:  ")
b= input("Enter the Second number of your choice: ")

print("Your Number of Choice before swapping", a)
print("Your Number of Choice after swapping", b)

a,b =b,a

print("New Value of your First number of choice after swapping is: ", a)
print("New Value of your Second number of choice after swapping is: ", b)

# 11. Check The Memory Usage Of the Variable

import sys

a= input("Write something which you want to display in size")
print("The memory size of what you typed is  :" ,(sys.getsizeof(a)))


# 12. Print string N times

a= input("Please type what you want to print 5 times")
b = a * 5
print(b)

# 13. Splitting a string into a list


a= "Hello! Is it me you are looking for?"

g = a.split()
print(g)

# 14. Display multiple input values in a single line


Brand, Model, Year, Location = input("Enter Brand, Model, Year and Location : ").split()
print(f'Brand is:', {Brand})
print(f'Model is:', {Model})
print(f'Year is: ', {Year})
print(f'Location is:', {Location})


#15. Give 3 incorrect names of the variables

age_*
+age
3age

#16. Give 3 correct names of the variables
age
_age
Age

# 17. What is the purpose of using variables?
to manipulate memory address easily, wecan attach a name to the memory address for variables

# 18. How can we define a constant variable? Give an example.

#19. What reserved Python keywords we can't use to define variables? Provide as many examples as you can.
any variable starting with number

