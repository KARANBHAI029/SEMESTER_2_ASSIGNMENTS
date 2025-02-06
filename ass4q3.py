def checkpangram(strg):
    list1=[0]*26
    for i in strg.lower():
        if i.isalpha():
            index = ord(i) - ord('a') 
            list1[index] += 1
    return all(count > 0 for count in list1)
input_string = "The quick brown fox jumps over the lazy dog"
print(checkpangram(input_string))  # Output: True