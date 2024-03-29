def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False
    
s1 = input().strip()
s2 = input().strip()


if is_anagram(s1, s2):
    print("YES")
else:
    print("NO")