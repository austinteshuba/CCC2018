# This solution is not fully correct due to time efficiency, but it gets the right answer

from pprint import *
import functools
line = input()
inputs = line.split()
n = int(inputs[0])
m = int(inputs[1])
#print(n,m)
#let 0 be not possible, let 1 be possible, let 2 be starting
graph=[]
startX=None
startY=None
steps=[]
for a in range(m):
    line=[]
    for b in range(n):
        line.append(-2)
    steps.append(line)
    
for s in range(n):
    l=input()
    #print(l)
    letters=list(map(str,l))
    xCount=0
    line = []
    for let in letters:
        if let == "W":
            line.append(0)
        elif let == ".":
            line.append(1)
            steps[s][xCount]=-1
        elif let == "S":
            line.append(2)
            startX = xCount
            startY = s
        else:
            line.append(0)
        xCount+=1
    graph.append(line)
#print(graph)
#rint(startX, startY)
#print(graph[startY][startX])

#pprint(graph)
steps[startY][startX]=0

@functools.lru_cache(maxsize=32)
def move (currentSteps, x, y):
    if graph[y][x]==0:
        return
    else:
        if steps[y][x]>=currentSteps+1 or steps[y][x]==-1:
            steps[y][x] = currentSteps+1
        #print(x,y)
        if x>1:
            if steps[y][x-1]<0 or steps[y][x-1]>=currentSteps+1:
                move(currentSteps+1, x-1, y)
        if y>1:
            if steps[y-1][x]<0 or steps[y-1][x]>=currentSteps+1:
                move(currentSteps+1, x, y-1)
        if x<len(graph[0])-1:
            if steps[y][x+1]<0 or steps[y][x+1]>=currentSteps+1:
                move(currentSteps+1, x+1,y)
        if y<len(graph)-1:
            if steps[y+1][x]<0 or steps[y+1][x]>=currentSteps+1:
                move(currentSteps+1, x, y+1)
        

move(-1, startX, startY)
#print(steps)

for a in steps:
    for b in a:
        if b!=-2 and b!=0:
            print(b)

