import requests

def sortList(varName):
    with open(varName, "r", encoding ="UTF-8") as file:
        for line in file:
            response = requests.get(line)
            if response.status_code == 200:
                    okFile = open("okList.txt", "a", encoding ="UTF-8")
                    okFile.write(line)
            okFile.close()
            
ListName = input("Enter Boss List Name : ")

sortList(ListName)
