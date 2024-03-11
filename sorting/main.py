import numpy as np 
import time

from divideAndConquer import quicksort

def __main__():
    rand_int = np.random.randint(0,15, 20)
    print(rand_int)
    start = time.time()
    # sortedList = selection_sort(rand_int)
    # sortedList = bubbleSort(rand_int)
    # sortedList = mergeSort(rand_int)
    sortedList = quicksort(rand_int)
    end = time.time()

    print(sortedList)
    duration = end -start
    print(duration)
    test(sortedList)

def test(l):
    for i in range(len(l)-1):
        assert(l[i] <= l[i+1])

def quicksort(list, left = 0, right = None):
    if right == None:
        right = len(list)-1

    if left < right:
        pivot = part(list, left, right)
        quicksort(list, left, pivot-1)
        quicksort(list, pivot + 1, right)
    return list

def part(list, left, right):
    pivot = list[right]
    _left = left
    _right = right
    while left < right:
        while right > _left and list[right] >= pivot:
            right -= 1
        while left < _right and list[left] < pivot:
            left += 1

        if left < right:
            list[left], list[right] = list[right], list[left]
        else:
            break
    if(list[left] > pivot):
        list[_right], list[left] = list[left], list[_right]
    
    return left

def merge(links, rechts):
    sortedList = []
    i = 0
    for l in links:
        while True:
            if i < len(rechts) and l > rechts[i]:
                sortedList.append(rechts[i])
                i += 1
            else: break
        sortedList.append(l)
    sortedList.extend(rechts[i:len(rechts)])
    return sortedList



#Combined with insertionSort
def mergeSort(liste):
    length = len(liste)
    if length <= 100:
        return insertion_sort(liste)
    else:
        sortedListLinks = mergeSort(liste[0:int(length/2)])
        sortedListRechts = mergeSort(liste[int(length/2): length])

    sortedList = merge(sortedListLinks, sortedListRechts)
    
    return sortedList


#Tausche immer wieder den aktuellen index mit dem nächsten falls aktueller größer ist
def bubbleSort(l):
    length = len(l)-1
    runs = 0
    while runs < length:
        for index, _ in enumerate(l):
            if(index == length - runs):
                break
            if(l[index] > l[index+1]):
                l[index + 1], l[index] = l[index], l[index + 1]
        runs += 1
    return l

#für jeden index wähle das minimum zwischen aktuellem index und dem Ende und setze 
#dieses auf den aktuellen Index
def selection_sort(l):
    length = len(l)
    print(length)
    for index in range(length):
        minIndex = index
        for _index in range(index+1, length):
            if(l[minIndex] > l[_index]):
                minIndex = _index
        l[minIndex], l[index] = l[index], l[minIndex]
    return l

#für jeden index tausche mit vorherigem Index solange dieser Größer ist
def insertion_sort(l):
    for index,_ in enumerate(l):
        while (index>0):
            if(l[index] < l[index - 1]):
                l[index -1], l[index] = l[index], l[index - 1]
            index -= 1
    return l


            
        




__main__()