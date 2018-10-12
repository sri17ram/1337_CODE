import logging

rom2int = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

def romanToInt(roman_input):

    sum = 0

    for index, value in enumerate(roman_input):
        if value == "I" and index != (len(roman_input)-1) and (roman_input[index+1] == "V" or roman_input[index+1] == "X"):
            if roman_input[index+1] == "V":
                sum = sum + 4
            elif roman_input[index+1] == "X":
                sum = sum + 9
        elif (value == "V" or value == "X") and index != 0 and roman_input[index-1] == "I":
            continue
        elif value == "X" and index != (len(roman_input)-1) and (roman_input[index+1] == "L" or roman_input[index+1] == "C"):
            if roman_input[index+1] == "L":
                sum = sum + 40
            elif roman_input[index+1] == "C":
                sum = sum + 90
        elif (value == "L" or value == "C") and index != 0 and roman_input[index-1] == "X":
            continue
        elif value == "C" and index != (len(roman_input)-1) and (roman_input[index+1] == "D" or roman_input[index+1] == "M"):
            if roman_input[index+1] == "D":
                sum = sum + 400
            elif roman_input[index+1] == "M":
                sum = sum + 900
        elif (value == "M" or value == "D") and index != 0 and roman_input[index-1] == "C":
            continue
        else:
            print(index, value, rom2int[value])
            sum = sum + rom2int[value]

    print("SUM => {}".format(sum))
    return sum

print (romanToInt("MCMXCIV"))