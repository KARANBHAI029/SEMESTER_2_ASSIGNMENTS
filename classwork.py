#finding by back rfind/rindex
str1="Karanra bhedara"
substring="ra"
for i in range(len(str1)-len(substring),-1,-1):
    if substring==str1[i:i+len(substring)]:
        print(i)
        break
else:
    print("not found")    

substring="ra"
for i in range(12,4,-1):
    if substring==str1[i:i+len(substring)]:
        print(i)
        break;
else:
    print("not found")    