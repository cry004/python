#Ask user for name
name = input("what is your name?: ")
print(name)
#Ask user for age
age = input("how is your age?: ")
#Ask user for city
city = input("what is your city?: ")
#Ask user what they enjoy
love = input("what do you love doning?: ")
#Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

#Print output to screen
print(output)
