scores_count = int(input())
s = list(map(int, input().rstrip().split()))
alice_count = int(input())
a = list(map(int, input().rstrip().split()))




s = list(dict.fromkeys(s)) #rule out duplicate values from list "s"
l = len(s)-1
for i in a:
    for j in range(l,-1,-1):
        if i < s[-1]:
            print(len(s)+1)
            break
        elif i > s[0]:
            print(1)
            break
        else:
            if s[j]>i:
                print(j+2)
                l = j #searching from this index instead from starting 
                break
            elif i == s[j]:
                print(s.index(i)+1)
                l = j #searching from this index instead from starting
                break





