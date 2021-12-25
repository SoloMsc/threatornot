import requests



class Test:
    def __init__(self, name, file, compare):
        self.n = name
        self.f = file
        self.c = compare

    def read(self):
        myList = []
        mike = open(self.f, "r")
        james = mike.readlines()
        for x in james:
            response = requests.post("https://davidduke.com/" + x)
            if response.status_code == 200:
                myList.append(x)
                print(x + "is valid")

            else:
                print(x + "is not valid")

        seby = open(self.c, "r")
        wiwi = seby.readlines()

        for x in myList:
            if x in myList and x in wiwi:
                print(x + "makes this likley a dangerous website!")




isis = Test("James","this.txt", "new.txt")

isis.read()





