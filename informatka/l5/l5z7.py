def anagram(s1,s2):
    s1=list(s1.upper())
    s2=list(s2.upper())
    s1.sort()
    s2.sort()
    print(s1==s2)
