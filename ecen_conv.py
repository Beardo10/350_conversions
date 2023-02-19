from bidict import bidict

hex_binary = bidict({ #represents one-to-one relatinship between pairs of hex and binary
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

digit_formats = { #for easy code reading
    "d'": "decimal",
    "b'": "binary",
    "0x": "hex"
}

#takes hex number, converts and links each hex value together
def hex_to_binary(hexNum):
    hexNum = hexNum[2:]
    binary = "b'"
    for num in hexNum:
        binary += hex_binary[num]
    return binary.lstrip("0")

#takes binary number, converts and links each bit to hex
def binary_to_hex(binNum): #DOES NOT WORK!
    binNum = binNum[2:]
    #must split binNum into chunks of 4
    splitNum = []

    while len(binNum) > 4: #split binary number into chunks of 4
        splitNum.append(binNum[:-5:-1])
        binNum = binNum[0:len(binNum) - 4]
    while len(binNum) < 4: #need to add leading zeros to MSB -------------- horribly inefficient, maybe fix later
        binNum = "0" + binNum
    splitNum.append(binNum)
    hexNum = "0x"
    for nums in reversed(splitNum):
        hexNum = hexNum + hex_binary.inverse[nums]
    return hexNum

#Takes 2^0, 2^1, 2^2... based on digit. Then add values up
def binary_to_decimal(binNum):
    binNum = binNum[2:]
    binNum = binNum[::-1] #reverses
    power = 0
    sum = 0
    for digit in binNum:
        if digit == "1":
            sum += 2 ** power
        power += 1
    return"d'" + str(sum)




#takes decimal value, modulus by 2 and record digit, then divide by 2 until number reaches 0. Then return reverse of string.
def decimal_to_binary(decNum):
    if decNum == "0":
        return "b'0"
    decNum = int(decNum[2:])
    binNum = ""
    while decNum != 0:
        binNum += str(decNum % 2)
        decNum //= 2
    return "b'" + binNum[::-1]



#takes one form, shows it in all three forms
def show_forms(num):
    if(digit_formats[num[0:2]] == "decimal"):
        print("Decimal: {}".format(num))
        print("Binary:  {}".format(decimal_to_binary(num)))
        print("Hex:     {}".format(binary_to_hex(decimal_to_binary(num))))
    if(digit_formats[num[0:2]] == "binary"):
        print("Decimal: {}".format(binary_to_decimal(num)))
        print("Binary:  {}".format(num))
        print("Hex:     {}".format(binary_to_hex(num)))
    if(digit_formats[num[0:2]] == "hex"):
        print("Decimal: {}".format(binary_to_decimal(hex_to_binary(num))))
        print("Binary:  {}".format(hex_to_binary(num)))
        print("Hex:     {}".format(num))


    
number = input()

while (number != "quit"):
    show_forms(number)
    number = input()








