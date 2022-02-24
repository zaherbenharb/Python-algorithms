#!/usr/bin/env python
# coding: utf-8

# In[19]:


def binary_search(A, l, h,k):
    if h >= l:
        mid = int(l + (h - l)/2)
        print(mid)
        if A[mid] == 6:
            return '6 is found'
        elif A[mid] > 6:
            return binary_search(A, l, mid-1, 6)
        else:
            return binary_search(A, mid+1, h, 6)
    else:
        return '6 is not found'

A=[1,2,3,5,8]
k=6;l=0; h=len(A)-1;
binary_search(A, l, h, k)


# In[20]:


def binary_search(A, l, h,k):
    if h >= l:
        mid = int(l + (h - l)/2)
        print(mid)
        if A[mid] == 5:
            return '5 is found'
        elif A[mid] > 5:
            return binary_search(A, l, mid-1, 5)
        else:
            return binary_search(A, mid+1, h, 5)
    else:
        return '5 is not found'

A=[1,2,3,5,8]
k=5;l=0; h=len(A)-1;
binary_search(A, l, h, k)


# In[27]:


a=int(input('donner un entier a'))
b=int(input('donner un entier b'))
def puissance (a,b) :
    return a**b
puissance(a,b)


# In[22]:


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist

nlist = [29,13,22,37,52,49,46,71,56]
bubbleSort(nlist)


# In[23]:


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [29,13,22,37,52,49,46,71,56]
mergeSort(myList)
print(myList)


# In[24]:


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        
        while low <= high and array[high] >= pivot:
            high = high - 1

       
        while low <= high and array[low] <= pivot:
            low = low + 1

       
        if low <= high:
            array[low], array[high] = array[high], array[low]
            
        else:
            
            break

    array[start], array[high] = array[high], array[start]

    return high


# In[25]:


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


# In[26]:


array = [29,13,22,37,52,49,46,71,56]
quick_sort(array, 0, len(array) - 1)
print(array)


# In[ ]:




