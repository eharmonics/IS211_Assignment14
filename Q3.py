def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1
    else:
        if s1[0] == s2[0]:
            return compareTo(s1[1:], s2[1:])
        else:
            return ord(s1[0]) - ord(s2[0])
        
print(compareTo("abc", "abc"))