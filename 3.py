# Реализуйте RLE алгоритм: реализуйте 
# модуль сжатия и восстановления данных.
inputlist = 'rrttggggggttyyyuutttuk'
print(inputlist)
result1 = []
result2 = []
temp = 1
zipStr = ''
unzipStr = ''
for i in range(len(inputlist)):
    if i == 0:
        result1.append(inputlist[i])
    else:
        if inputlist[i] == inputlist[i-1]:
            temp += 1
            if i == len(inputlist)-1:
                result2.append(temp)    
        else:
            result1.append(inputlist[i]) 
            result2.append(temp)
            temp = 1
            if i == len(inputlist)-1:
                result2.append(temp) 
for i in range(len(result2)):
    zipStr += str(result2[i])+result1[i] 
print(zipStr)
for i in range(0,len(zipStr),2):
    for j in range(int(zipStr[i])):
        unzipStr += str(zipStr[i+1])
print(unzipStr)


