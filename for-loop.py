#for i in range(1,11):
#    print(i)
#for letter in "abcd":
#    print(letter)
#for num in [1,2,3,4,5,6,7,8]:
#    print(num)

vowels = 0
consonants = 0

for letter in "asdjdlkrtnmqioeuqowhkjf":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
      
