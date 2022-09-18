from lib2to3.pgen2 import token
import re

def clipTest(clip):
    for key in clip.keys():
        print(f"{key}: {clip[key]}")

    return 0


clippingsFile = open("input\My Clippings.txt", "r", encoding="UTF-8")
allClippings = clippingsFile.read()
clippingsFile.close()
listOfClippings = allClippings.split("==========\n")

tokens={ #italian for now
    "bookmark": "Il tuo segnalibro",
    "highlightPage": "La tua evidenziazione",
    "note": "La tua nota",
    "date": "Aggiunto in data"
}

typesOfClip = {"bookmark", "highlightPage", "note"}


print(len(listOfClippings))

i= 0
for clipping in listOfClippings:
    clippingDict = {}
    linesOfClipping = clipping.splitlines()
    # linesOfClipping[0] #name and author
    # linesOfClipping[1] #type of highlight, page/position and date
    # linesOfClipping[2] #nothing
    # linesOfClipping[3] #highlight or note
    clippingDict["name"]= re.findall("^.*(?=\()",linesOfClipping[0])[0]
    clippingDict["author"]= linesOfClipping[0].replace(clippingDict["name"]," ").replace("(","").replace(")","")
    for type in typesOfClip:
        if(re.search(tokens[type],linesOfClipping[1])): clippingDict["type"]=type
    clippingDict["highlight"] = linesOfClipping[3]

    clipTest(clippingDict)
    i +=1
    if ( i == 50): break