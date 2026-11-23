def createFile(name, age):
    file = name+ str(age)
    with open(file, 'w') as file:
        file.write(name+str(age))

if __name__ == "__main__":
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    address = input("Enter your address:")
    createFile(name,age)
    print("Your name is",name)
    print("Your age is",age)
    print("Your address is", address)
