def add(*numbers):
	total = 0
	for number in numbers:
		total = total + number
	return (total)
print(add(1,2,3,4,5,6,7,8,9))

def about(name, age, like):
    sentence = "Meet {}! They are {} years old and like {}".format(name,age,like)
    return sentence

dictionary = {"name":"ZZZ", "age": 23, "like": "Python"}
print(about(**dictionary))

def foo(**kk):
    for key,value in kk.items():
        print("{}:{}".format(key,value))
foo(huda="Female", z="male", john="male")
