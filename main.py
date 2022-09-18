import re

def clipTest(clip):
    for key in clip.keys():
        print(f"{key}: {clip[key]}")

    return 0


clippingsFile = open("input\My Clippings.txt", "r", encoding="UTF-8")
allClippings = clippingsFile.read()
clippingsFile.close()
listOfClippings = allClippings.split("==========\n")

tokensLanguageDependeant={ #italian for now
    "bookmark": "Il tuo segnalibro",
    "highlightPage": "La tua evidenziazione a pagina",
    "note": "La tua nota a",
    "highlightPosition": "Il tuo segnalibro alla posizione",
    "date": "Aggiunto in data"
}


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
    linemodified= linesOfClipping[0].replace(clippingDict["name"]," ")
    linemodified= linemodified.replace("(","")
    linemodified= linemodified.replace(")","")
    clippingDict["author"]= linesOfClipping[0].replace(clippingDict["name"]," ").replace("(","").replace(")","")
    clipTest(clippingDict)

    i +=1
    if ( i == 4): break