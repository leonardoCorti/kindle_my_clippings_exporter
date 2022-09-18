
def clipTest(clip):
    for key in clip.keys():
        print(f"{key}: {clip[key]}")

    return 0


clippingsFile = open("input\My Clippings.txt", "r", encoding="UTF-8")
allClippings = clippingsFile.read()
clippingsFile.close()
listOfClippings = allClippings.split("==========")

tokensLanguageDependeant={ #italian for now
    "bookmark" : "Il tuo segnalibro",
    "date" : "Aggiunto in data"
}


print(len(listOfClippings))

i= 0
for clipping in listOfClippings:
    clippingDict = {}
    #print(len(clipping.splitlines()))
    #print(clipping)
    for line in clipping.splitlines():
        print(f"a\n {line.strip()}\nb")
    
    i +=1
    if ( i == 4): break