class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charc = s
        maxsubstr = 0
        arr = []
        for cha in charc:
            #print(cha)
            if len(arr) == 0:
                #print("Yes, I am")
                arr.append(cha)
            else:
                if cha not in arr:
                    arr.append(cha)
                else:
                    #print (arr.index(cha)+1)
                    for i in range(arr.index(cha), -1, -1):
                        #print ("Index Of" + str(i))
                        arr.pop(i)
                    arr.append(cha)
            #print(arr, len(arr))
            if len(arr) > int(maxsubstr):
                maxsubstr = len(arr)
        return maxsubstr



    #############################################33

    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            maxsubstr = 0
            arr = []
            for cha in s:
                if len(arr) == 0:
                    arr.append(cha)
                else:
                    if cha not in arr:
                        arr.append(cha)
                    else:
                        for i in range(arr.index(cha), -1, -1):
                            arr.pop(i)
                        arr.append(cha)
                if len(arr) > int(maxsubstr):
                    maxsubstr = len(arr)
            return maxsubstr




