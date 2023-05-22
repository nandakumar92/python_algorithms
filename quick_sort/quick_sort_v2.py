# https://www.youtube.com/watch?v=7h1s2SojIRw&t=717s
# easy to understand version of quicksort

def partition(lst,l,h):
    pivot=l
    i=l
    j=h
 
    while i<j: 
        while lst[i]<=lst[pivot] and i<h:
            i+=1            
        while lst[j]>lst[pivot] and j>pivot:
            j-=1
        if i<j:
            lst[i],lst[j]=lst[j],lst[i]

    return j
        
def quick_sort(lst,l,h):
  
    if (h-l+1)>=2:## atleast 2 elemets or can use if l<h.Both are same, atleast two elements in each recursive call.
        pi=partition(lst,l,h)
        quick_sort(lst,l,pi-1)
        quick_sort(lst,pi+1,h)
    return lst
 
x=[5,5,4,1,2,3,8,8,6]
y=quick_sort(x,0,len(x)-1)
print(y)
        


