def intersection(nums1, nums2):
    inter = [0]*1001
    result = []
    for i in range(len(nums1)):
        inter[nums1[i]] = 1
    
    
    for i in range(len(nums2)):
        if(inter[nums2[i]] == 1):
            inter[nums2[i]] = 3
    
    for k in range(len(inter)):
        if(inter[k] == 3):
            result.append(k)
    
    return result