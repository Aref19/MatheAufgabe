def BinearToDecimal(BinearList):
    lengh = len(BinearList) - 1
    result = 0
    for i in BinearList:
        if (i == 1):
         result += 2 ** lengh
         print(result)
        lengh = lengh - 1

    print(f'le,{lengh}')




def decimalToBineare(zahl):
    return bin(zahl)


print(decimalToBineare(8))