clippingsFile = open("input\My Clippings.txt", "r", encoding="UTF-8")
allClippings = clippingsFile.read()
clippingsFile.close()

listOfClippings = allClippings.split("==========")

print(len(listOfClippings))

i= 0
for line in listOfClippings:
    i +=1
    print(line.strip())
    print("\n\n")
    if ( i == 10): break
