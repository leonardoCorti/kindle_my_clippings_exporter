import re

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

for clipping in listOfClippings:
    clippingDict = {}
    linesOfClipping = clipping.splitlines()
    # linesOfClipping[0] #name and author
    # linesOfClipping[1] #type of highlight, page/position and date
    # linesOfClipping[2] #nothing
    # linesOfClipping[3] #highlight or note
    if(len(linesOfClipping)<4): break
    if(re.match("^.*(?=\()",linesOfClipping[0])):
        clippingDict["name"]= re.findall("^.*(?=\()",linesOfClipping[0])[0]
        clippingDict["author"]= linesOfClipping[0].replace(clippingDict["name"]," ").replace("(","").replace(")","")
    else: clippingDict["name"]= linesOfClipping[0]
    for type in typesOfClip:
        if(re.search(tokens[type],linesOfClipping[1])): clippingDict["type"]=type
    clippingDict["highlight"] = linesOfClipping[3]
    outputFileName= "output\\"+clippingDict["name"].strip().replace("/","")+".md"
    output = open(outputFileName, "a", encoding="UTF-8")
    if(clippingDict["type"] != "bookmark"):output.write(f"{clippingDict['type']}:\n{clippingDict['highlight']}\n\n")
    output.close()