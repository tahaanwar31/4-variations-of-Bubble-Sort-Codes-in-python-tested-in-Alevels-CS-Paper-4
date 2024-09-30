ArrayData=[10,5,3,7,8,34,97,32,12,3225,1111]
def BubbleSort():
    global ArrayData
    for x in range(len(ArrayData)):
        for y in range(len(ArrayData)-1):
            if ArrayData[y]>ArrayData[y+1]:
                temp=ArrayData[y]
                ArrayData[y]=ArrayData[y+1]
                ArrayData[y+1]=temp
BubbleSort()
def BubbleSort1():
    global ArrayData
    for x in range(len(ArrayData)):
        for y in range(len(ArrayData)-x-1):
            if ArrayData[y]>ArrayData[y+1]:
                temp=ArrayData[y]
                ArrayData[y]=ArrayData[y+1]
                ArrayData[y+1]=temp
BubbleSort1()
def BubbleSort2():
    global ArrayData
    boundary=len(ArrayData)-1
    for x in range(len(ArrayData)):
        for y in range(boundary):
            if ArrayData[y]>ArrayData[y+1]:
                temp=ArrayData[y]
                ArrayData[y]=ArrayData[y+1]
                ArrayData[y+1]=temp
        boundary=boundary-1
BubbleSort2()
def BubbleSort3():
    global ArrayData
    boundary=len(ArrayData)-1
    noswaps=False
    while noswaps==False:
        noswaps=True
        for x in range(boundary):
            if ArrayData[x]>ArrayData[x+1]:
                temp=ArrayData[x]
                ArrayData[x]=ArrayData[x+1]
                ArrayData[x+1]=temp
                noswaps=False
        boundary=boundary-1
BubbleSort3()
print(ArrayData)


