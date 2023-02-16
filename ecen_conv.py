from bidict import bidict

hex_binary = bidict({
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
})

#takes hex number, converts and links each hex value together
def hex_to_binary(hexNum):
    binary = ""
    for num in hexNum:
        binary += hex_binary[num]
    return binary.lstrip("0")

def binary_to_hex(binNum):
    #must split binNum into chunks of 4
    splitNum = []

    while len(binNum) > 4: #split binary number into chunks of 4
        splitNum.append(binNum[:-5:-1])
        binNum = binNum[0:len(binNum) - 4]
    if len(binNum) != 4: #need to add leading zeros to MSB
        binNum.rjust(4-len(binNum))
    splitNum.append(binNum)

    hexNum = ""
    for nums in splitNum:
        hexNum += hex_binary.inverse[nums]
    return hexNum


    # hex = ""
    # for num in binNum:
    #     hex += hex_binary.inverse[num]
    # return hex.lstrip("0")

print(binary_to_hex("00001111"))








