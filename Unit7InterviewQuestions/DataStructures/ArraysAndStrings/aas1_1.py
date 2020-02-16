# HInts: 44,117,132

#!/usr/bin/python3

str1="hello"
str2="helo"
str3="hello world"

# brute force method to check duplicates

def hasUnique(sampleString):
    for i in range(0,len(sampleString)):
        for j in range(i+1,len(sampleString)):
            if(sampleString[i]==sampleString[j]):
                return False
    return True

# print("Does String1 has uniques: ",hasUnique(str1))
# print("Does String2 has uniques: ",hasUnique(str2))
# print("Does String3 has uniques: ",hasUnique(str3))

# hashing method to check uniques
listAlpha=[0 for x in range(0,52)]
def hasUniqueByHash(sampleString):
    for i in sampleString:
        listAlpha[ord(i)-95]+=1
    for j in listAlpha:
        if j>1:
            return False
    return True 

# print(hasUniqueByHash(str2))

def hasUniqueByNLogN(sampleString):
    print("Checking string "+ sampleString)
    tempString=''.join(sorted(sampleString))
    for i in range(0,len(tempString)-1):
        if(tempString[i]==tempString[i+1]):
            return False
    return True
print(hasUniqueByNLogN(str1))

#TODO: 
# 1.use user inputs
# 2.use sorting algorithm
# 3.use bit vector 
