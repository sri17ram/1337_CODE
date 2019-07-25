# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

def bin2data(a, b):
        # CARRY-IN, INT-1, INT-2: CARRY-OUT, SUM
    b2d_sum = {
           '000': [0, 0],
           '001': [0, 1],
           '010': [0, 1],
           '011': [1, 0],
           '100': [0, 1],
           '101': [1, 0],
           '110': [1, 0],
           '111': [1, 1]
           }
    diff = int(len(a)) - int(len(b))
    # print ('DIFF = {}; Type = {}'.format(diff, type(diff)))

    if diff > 0:
        for i in range(diff):
            b = '0' + b
    elif diff < 0:
        diff = abs(diff)
        for i in range(diff):
            a = '0' + a

    # print(len(a), len(b), a, b)

    CARRY_IN = 0
    final = ''

    for j in range(1, len(a)+1):
        [CARRY_OUT, SUM] = b2d_sum[str(CARRY_IN) + str(a[-j]) + str(b[-j])]
        # print (CARRY_OUT, SUM)
        final = str(SUM) + final
        CARRY_IN = CARRY_OUT
    if CARRY_IN:
        final = str(CARRY_IN) + final
    print (final)
    exit()

bin2data("11","1")