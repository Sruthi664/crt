# Enter your code here
def binary_search(arr,target):
    #calculate start,end mid values
    start=0
    end=len(arr)-1
    mid=(start+end)//2  #important
    #while loop:
    while(start<=end):
        if(arr[mid]==target):
            return mid
        elif(target>arr[mid]):
            start=mid+1
        else:
            end=mid-1
        mid=(start+end)//2
    return -1   #if not found return -1
arr=[4,5,6,7,8,9,10,11,12]
target=7
result=binary_search(arr,target)
print(result)

def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        mid = (start + end) // 2
        # Recursively sort the first half
        merge_sort(arr, start, mid)
        # Recursively sort the second half
        merge_sort(arr, mid + 1)
        # Merge the sorted halves
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]
    i = j = 0
    k = start
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [30, 12, 4, 49, 45]
merge_sort(arr)
print(arr)


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    left=[]
    right=[]
    equal=[]
    pvt=arr[-1]
    for i in arr:
        if(i<pvt):
            left.append(i)
        elif(i>pvt):
            right.append(i)
        else:
            equal.append(i)
            print("pivot:",pvt)
            #partitioning the array into three lines
            print("left sub array",left)
            print("right sub array",right)
            print("equal array",equal)
            return quick_sort(left)+equal+quick_sort(right)
arr=[23,63,44,57,12,45,36]
sorted_arr = quick_sort(arr)
print(sorted_arr)


def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[45,8,9,3]
sorted_arr=bubble_sort(arr)
print(sorted_arr)