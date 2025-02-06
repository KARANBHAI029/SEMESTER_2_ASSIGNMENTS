def checkpalindrome(strg):
    l = len(strg) - 1
    for i in range(len(strg) // 2):
        if strg[i] != strg[l - i]:  
            return False  
    return True 


def makepalindrome(strg):
    if checkpalindrome(strg):  
        return strg, 0 

    length = len(strg) - 1
    strg_list = list(strg)  
    reduction_count = 0  

    for i in range(len(strg) // 2):
        while strg_list[i] != strg_list[length - i]:
            
            if strg_list[length - i] > strg_list[i]:
                strg_list[length - i] = chr(ord(strg_list[length - i]) - 1)
            else:
                strg_list[i] = chr(ord(strg_list[i]) - 1)

            reduction_count += 1 

    return "".join(strg_list), reduction_count 


strg1 = "abc"
result, count = makepalindrome(strg1)
print(f"Input: {strg1} → Output: {result}, Reductions: {count}")

strg2 = "abcba"
result, count = makepalindrome(strg2)
print(f"Input: {strg2} → Output: {result}, Reductions: {count}")

strg3 = "abcd"
result, count = makepalindrome(strg3)
print(f"Input: {strg3} → Output: {result}, Reductions: {count}")
