
import enchant
from itertools import  permutations

d = enchant.Dict("en_US")

wordstt = ["LORE", "HERO", "CANT", "SURE", "SELL", "KINE", "PEON", "LICE", "ALTI", "RISE", "LINK", "LIRA", "IMAM", "FONE", "CALM", "FENCE", "CONIC", "NURSE", "VALES", "RETAG", "STAMP", "ALTER", "DEBATE", "THETICAL"]

conlst = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
vowlst = ["A",  "E",  "I", "O", "U", "Y"]

wiff = []

for elem in conlst:

    for elem2 in vowlst:

        wiff.append([elem, elem2])
        wiff.append([elem2, elem])

solvlst = []

for wd in wordstt:
    z = len(wd) + 4
    minilst = []
    sublst = []
    for el in wd:
        sublst.append(el)
    
    for rog in wiff:

        sub2lst = []
        sub2lst.append(rog[0])
        sub2lst.append(rog[1])
        sub2lst.append(rog[0])
        sub2lst.append(rog[1])

        for tab in sublst:
            sub2lst.append(tab)
        wigg = list(permutations(sub2lst, z))

        for trob in wigg:

            teststr = ""

            for lat in trob:
                teststr += lat

            if d.check(teststr) and teststr not in minilst:

                print(teststr)
                minilst.append(teststr)
                   

    solvlst.append(minilst)

print(solvlst)









