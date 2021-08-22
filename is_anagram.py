def isAnagram(s,t):
    holder_s = [0]*26
    holder_t = [0]*26
    if(len(s) != len(t)):
        return False
    for i in range(len(s)):
        holder_s[ord(s[i]) - 97] += 1
    for i in range(len(t)):
        holder_t[ord(t[i]) -97] += 1
    
    return holder_t == holder_s