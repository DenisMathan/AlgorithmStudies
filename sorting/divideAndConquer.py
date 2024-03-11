

#Teile anhand eines Pivot-Elements das Array in zwei teile und sortiere alle anderen elemente links und rechts davon ein
# mache dies solange linke grenze kleiner rechte Grenze ist
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


#Kombiniert mit insertion-Sort noch schneller
def mergeSort(liste):
    length = len(liste)
    if length < 1:
        sortedListLinks = mergeSort(liste[0:int(length/2)])
        sortedListRechts = mergeSort(liste[int(length/2): length])

    sortedList = merge(sortedListLinks, sortedListRechts)
    
    return sortedList


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



        