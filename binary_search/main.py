def binary_search(arr,left,right,val):
    while left<right:
        mid=(left+right)//2
        if val==arr[mid]:
            return True
        elif val>arr[mid]:
            return binary_search(arr,mid+1,right,val)
        else:
            return binary_search(arr,left,mid-1,val)
    return False

x=[2,3,6,7,8]
print(binary_search(x,0,len(x)-1,10))