known_user = ["Alice","Bob","Clair","Dan","Emma"]
print(len(known_user))

while True:
    print("Hi!My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_user:
        print("name recognised")
    else:
        print("name Not recognised")
