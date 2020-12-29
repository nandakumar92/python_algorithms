def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr

def partition(arr,low,high):
    temp=low
    pivot=high
    for i in range(low,high):
        if arr[i]<arr[pivot]:
            arr[temp],arr[i]=arr[i],arr[temp]
            temp+=1
    arr[pivot],arr[temp]=arr[temp],arr[pivot]
    return temp

def quicksort_easy(arr):
    if len(arr)<=1:
        return arr
    small,larger,equal=[],[],[]
    pivot=arr[0]
    for i in arr:
        if i<pivot:
            small.append(i)
        elif i>pivot:
            larger.append(i)
        else:
            equal.append(i)
    return quicksort_easy(small)+equal+quicksort_easy(larger)

x=[2,8,5,3,4]
print(quicksort_easy(x))
x=[2,8,5,3,4]
print(quicksort(x,0,len(x)-1))
