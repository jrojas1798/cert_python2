#Laboratorio 2.3.1.18
def mysplit(strng):
    if strng =='' or strng.isspace():
        return [ ]
    lst = []
    word = ''
    inword = not strng[0].isspace()
    for x in strng:
        if inword:
            if not x.isspace():
                word = word + x
            else:
                lst.append(word)
                inword = False
        else:
            if not x.isspace():
                inword = True
                word = x
            else:
                pass
    if inword:
        lst.append(word)
    return lst


print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
