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


print(ToBinear(127))
key=['','','','','','','','','','','','','']
def HExToDecimal(zahl):




