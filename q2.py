n = int(input())
increment = 0
table = []
for x in range(n):
    table.append([int(x) for x in input().split()])
#print(table)

#check for increments clockwise
#check if it is increasing horizontally to the right
increasingH = None
for y in range(len(table)):
    for x in range(1, len(table[y])):
        if table[y][x] - table[y][x-1]>0:
            increasingH=True
        else:
            increasingH=False

#check vertically if it is increasing downwards
increasingV=None
for y in range(1,len(table)):
    for x in range(len(table[y])):
        if table[y][x] > table[y-1][x]:
            increasingV = True
        else:
            increasingV = False
#print(increasingH, increasingV)

if increasingH:
    if increasingV:
        output=""
        for ele in table:
            for item in ele:
                output+="%s "%(item)
            print(output)
            output=""
    else:
        for x in range(len(table)):
            output=""
            for y in range(len(table)):
                output+="%s "%(table[len(table)-y-1][x])
            print(output)
else:
    if increasingV:
        for x in range(len(table)):
            output=""
            for y in range(len(table)):
                output+="%s "%(table[y][len(table)-x-1])
            print(output)
    else:
        for x in range(len(table)):
            output=""
            for y in range(len(table)):
                output+="%s "%(table[len(table)-x-1][len(table)-y-1])
            print(output)


