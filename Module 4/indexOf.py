'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
def strStr(haystack, needle):
  if needle == "":
    return 0
  if needle not in haystack:
    return -1
  else:
    return len(haystack.split(needle)[0])

print(strStr("word","r"))#returns 3
print(strstr("word","rp")) #returns -1
