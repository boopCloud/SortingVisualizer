import time

# bubble sort
def bubble_sort(data, drawData, speed):
    for i in range(0, len(data)-1):
        swapped=False
        for j in range(0, len(data)-i-1):
            if data[j]>data[j+1]:
                swapped=True
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [r'#5f27cd' if x==j or x==j+1 else r'#34495e' for x in range(len(data))])
                time.sleep(speed)
        if not swapped:
            break
    drawData(data, [r'#5f27cd' for _ in range(len(data))])

# selection sort
def selection_sort(data, drawData, speed):
    for i in range(0, len(data)-1):
        smallest = i
        for j in range(i+1, len(data)):
            if data[smallest]>data[j]:
                smallest=j
                time.sleep(speed)
        data[smallest], data[i] = data[i], data[smallest]
        drawData(data, [r'#5f27cd' if x==smallest or x==i else r'#34495e' for x in range(len(data))])
    drawData(data, [r'#5f27cd' for _ in range(len(data))])

# insertion sort
def insertion_sort(data, drawData, speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while(j>=0 and data[j]>key):
            data[j+1]=data[j]
            drawData(data, [r'#5f27cd' if x==j+1 or x==j else r'#34495e' for x in range(len(data))])
            j-=1
            time.sleep(speed)
        data[j+1]=key
    drawData(data, [r'#5f27cd' for _ in range(len(data))])

# Merge Sort algorithm
def MergeSort(data, drawData, speed):
    Merge_Sort_Algo(data, 0, len(data)-1, drawData, speed)
    # drawData(data, [r'#5f27cd' for _ in range(len(data))])

def Merge_Sort_Algo(data, left, right, drawData, speed):
    if left<right:
        middle = left+(right-left)//2
        Merge_Sort_Algo(data, left, middle, drawData, speed)
        Merge_Sort_Algo(data, middle+1, right, drawData, speed)
        Merge(data, left, middle, right, drawData, speed)

def Merge(data, left, middle, right, drawData, speed):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(speed)

    n1=middle-left+1
    n2=right-middle
    leftPart=[]
    rightPart=[]

    for i in range(0, n1):
        leftPart.append(data[left+i])

    for j in range(0, n2):
        rightPart.append(data[middle+j+1])

    i=0
    j=0
    k=left
    while i<n1 and j<n2:
        if leftPart[i]<=rightPart[j]:
            data[k]=leftPart[i]
            i+=1
            k+=1
        else:
            data[k]=rightPart[j]
            j+=1
            k+=1
    
    while i<n1:
        data[k]=leftPart[i]
        i+=1
        k+=1
    while j<n2:
        data[k]=rightPart[j]
        j+=1
        k+=1

    drawData(data, ['#5f27cd' if x>=left and x<=right else '#34495e' for x in range(len(data))])
    time.sleep(speed)

def getColorArray(length, left, middle, right):
    colorArr=[]

    for i in range(length):
        if i>= left and i<=right:
            if i<=middle:
                colorArr.append('#e67e22')
            else:
                colorArr.append('#2ecc71')
        else:
            colorArr.append('#34495e')

    return colorArr

