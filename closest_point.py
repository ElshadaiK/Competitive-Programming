import math

def kClosest(points, k):
    d = {}
    result = []
    for i in range(len(points)):
        dist = distance(points[i])
        if(d.get(dist)):
            d[dist].append(points[i])
        else:
            d[dist] = [points[i]]

    while(len(result) < k):
        shortest = (min(d.keys()))
        for i in range(len(d[shortest])):
            result.append(d[shortest][i])
        d.pop(shortest)
    return result
    
def distance(point):
    return math.sqrt((point[0])**2 + (point[1])**2)

print(kClosest([[1,3],[-2,2]], 1))