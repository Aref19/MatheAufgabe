from builtins import dict

import Aufgabe3


def ToBinear(zahl):
    listm = []
    print(f'le,{listm}')
    while zahl != 0:
        if (int(zahl) % 2 != 0):
            listm.append(1)

            print(f'2,{zahl}')
            if (int(zahl) < 1):
                zahl = 0
                break
        else:
            #   print(f'le,{zahl}')
            if (int(zahl) < 1):
                zahl = 0
                break
            listm.append(0)

        zahl = int(zahl) / 2
        print(f'0,{zahl}')
    listm.reverse()
    print(f'le,{listm}')


#print(ToBinear(127))
key = dict({"0":0,"1": 1, "2": 2, "3":3, "4": 4, "5":5
               , "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,

            })


def HExToDecimal(zahl,true):
    wert=0
    list=[]
    for i in zahl:
       list.append(i)
    lengh = len(list)-1
    for y in list:
        wert+=key[y]*(16**lengh)
        print(f'dsa,{lengh}{key[y]}')
        lengh = lengh - 1
    print(lengh)
    if(true):
        ToBinear(wert)

    print(wert)


HExToDecimal("FC2",True)