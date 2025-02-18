t = int(input())  # Number of test cases

for _ in range(t):
    w = input().strip()
    word = list(w)
    
    for i in range(len(word) - 1, 0, -1):
        if ord(word[i]) > ord(word[i - 1]):
            word[i], word[i - 1] = word[i - 1], word[i]
            word = word[:i] + sorted(word[i:])
            print("".join(word))
            break
    else:
        print("no answer")  # If no break occurs, print "no answer"
