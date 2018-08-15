n = int(input())# amount of villages
points = []
for x in range(n):
    points.append(int(input()))
#print(points)
points.sort()
distances = 100000000000000
for pointIndex in range(1,len(points)-1):
    dist = 0
    dist += (points[pointIndex] - points[pointIndex-1])/2
    dist += (points[pointIndex+1] - points[pointIndex])/2
    if dist<distances:
        distances = dist
print(distances)
