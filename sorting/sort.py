
def selection_sort(arr):
    for i in range(len(arr)):
        minidx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minidx]:
                minidx=j
        arr[i],arr[minidx]=arr[minidx],arr[i]
    return arr

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
            else:
                break
    return arr

x=[2,8,1,3,4,5]
print(selection_sort(x))
x=[2,8,1,3,4,5]
print(bubble_sort(x))
x=[2,8,1,3,4,5]
print(insertion_sort(x))

