import os
import re

def readClippings():
    clippingsFile = open("input\My Clippings.txt", "r", encoding="UTF-8")
    allClippings = clippingsFile.read()
    clippingsFile.close()
    listOfClippings = allClippings.split("==========\n")
    return listOfClippings

def writeOutput(clippingDict):
    outputFileName= "output\\"+clippingDict["name"].strip().replace("/","")+".md"
    output = open(outputFileName, "a", encoding="UTF-8")
    if(clippingDict["type"] != "bookmark"):output.write(f"{clippingDict['type'].strip()}:\n{clippingDict['highlight'].strip()}\n\n")
    output.close()

def analyzeHighlight(tokens, typesOfClip, linesOfClipping):
    # linesOfClipping[0] #name and author
    # linesOfClipping[1] #type of highlight, page/position and date
    # linesOfClipping[2] #nothing
    # linesOfClipping[3] #highlight or note
    clippingDict = {}
    name(linesOfClipping, clippingDict)

    for type in typesOfClip:
        if(re.search(tokens[type],linesOfClipping[1])): clippingDict["type"]=type

    clippingDict["highlight"] = linesOfClipping[3]
    return clippingDict

def name(linesOfClipping, clippingDict):
    if(re.match("^.*(?=\()",linesOfClipping[0])):
        clippingDict["name"]= re.findall("^.*(?=\()",linesOfClipping[0])[0] 
        clippingDict["author"]= linesOfClipping[0].replace(clippingDict["name"]," ").replace("(","").replace(")","")
    else: clippingDict["name"]= linesOfClipping[0]

tokens={ #italian at the moment
    "bookmark": "Il tuo segnalibro",
    "highlightPage": "La tua evidenziazione",
    "note": "La tua nota",
    "date": "Aggiunto in data"
}
typesOfClip = {"bookmark", "highlightPage", "note"}

if not os.path.isdir('output'): os.mkdir('output') #generating output folder
listOfClippings = readClippings()

for clipping in listOfClippings:
    linesOfClipping = clipping.splitlines()
    if(len(linesOfClipping)<4): break #skip lines that aren't real highlight

    clippingDict = analyzeHighlight(tokens, typesOfClip, linesOfClipping)
    
    writeOutput(clippingDict)