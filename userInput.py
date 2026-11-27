import requests

def createFile(val):
    with open(val, 'w') as file:
        file.write(name+str(age))

def readWiki():
    url = "https://en.wikipedia.org/wiki/The_Red_Bottoms_Tour"
    headers = {
        "User-Agent": "LearningRAG/1.0 (educational project)"
    }
    response = requests.get(url,headers=headers, timeout=15)
    html= response.text
    title = html.split("<title>")[1].split("</title>")[0]
    return title

if __name__ == "__main__":
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    address = input("Enter your address:")
    val = name + str(age)
    createFile(val)
    print("Your name is",name)
    print("Your age is",age)
    print("Your address is", address)
    wiki = readWiki()
    createFile(wiki)
