import math, re
def isPali(strg):
    t = ''
    for i in strg:
        if re.search("[A-Z]|[a-z]|[0-9]",i):
            t = str(t) + str(i)
    strg = t
    for i in range(math.floor(len(strg)/2)):
        if (strg[i].lower() != strg[-1-i].lower()):
            return False
    return True
stat = isPali("A man, a plan, a canal: Panama")