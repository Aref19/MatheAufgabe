def BinearToDecimal(binearList):
    lengh = len(binearList) - 1
    result = 0
    for i in binearList:
        if (i == 1):
         result += 2 ** lengh
         print(result)
        lengh = lengh - 1

    print(f'le,{lengh}')




def decimalToBineare(zahl):
    return bin(zahl)


print(decimalToBineare(-4))