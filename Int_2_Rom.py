import math

int2rom = {
    1:"I",
    4:"IV"
    5:"V",
    9:"IX"
    10:"X",
    50:"L"
}
"""

for num in range(1, 40):
    # print(num)
    if (1 <= num%5<= 3):
        prefix_count = math.floor(num %10)
        if (1 <= prefix_count <= 3):
            prefix_count = math.floor(num%5)
            prefix_count_10 = math.floor(num/10)
            roman = str(int2rom[10])*prefix_count_10 + str(int2rom[1])*prefix_count
        elif ( 6 <= prefix_count <= 8):
            prefix_count = math.floor(num%5)
            prefix_count_10 = math.floor(num/10)
            roman=str(int2rom[10])* prefix_count_10 + str(int2rom[5]) + str(int2rom[1])*prefix_count
        print ("{} -> {}".format(num, roman))
    elif (num % 10 == 4 or num % 10 == 9 ):
        prefix_count = math.floor(num/10)
        roman = str(int2rom[10])*prefix_count+str(int2rom[1]) + str(int2rom[num%10+1])
        print("{} -> {}".format(num,roman))
    elif (num % 5  == 0 and num % 10 != 0):
        prefix_count = math.floor(num/10)
        roman = str(int2rom[10])*prefix_count+str(int2rom[5])
        print("{} -> {}".format(num,roman))
    elif (num %10 == 0 and num % 50 != 0):
        prefix_count = math.floor(num/10)
        roman = str(int2rom[10])*prefix_count
        print("{} -> {}".format(num, roman))
"""

for num in range (1, 40):
    final
    if (num >= 10):
        pc_10 = math.floor(num/10)
        num = num - pc_10 *10
        roman = str(int2rom[10])*pc_10
    if (6 <= num <= 8):
        pc_5 = math.floor(num/5)
        num = num - 5
        roman = roman + str(int2rom[5])
    if (num == 4):
        pc_4 = 1
    if (num > 0):
        pc_1 = num

