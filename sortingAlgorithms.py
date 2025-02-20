#/usr/bin/python3
import random

def random_sort():
    sorts = []
    sorts.append(bubble_sort)
    sorts.append(merge_sort)
    sorts.append(selection_sort)
    sorts.append(shell_sort)
    sorts.append(bogo_sort)
    sorts.append(gnome_sort)
    sorts.append(insertion_sort)
    sorts.append(heap_sort)
    sorts.append(quick_sort)
    return random.choice(sorts)

def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]     # Swap!
                yield # on every item write

# New indexing function that includes the right index.
def get_partial_list(origin_list, left_index, right_index): # Added
    return origin_list[left_index:right_index+1]

def MERGE(A,start,mid,end):
    L = get_partial_list(A,start,mid)
    R = get_partial_list(A,mid+1,end)
    i = 0
    j = 0
    k = start
    for l in range(k,end+1):            # changed
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1  
        yield

def merge_sort(A,p=0,r=-1):
    if r < 0:
        r = len(A)-1
    if r - p > 0:                          # changed
        mid = int((p+r)/2)
        yield from merge_sort(A,p,mid)
        yield from merge_sort(A,mid+1,r)             # changed
        yield from MERGE(A,p,mid,r)

def selection_sort(collection):
    length = len(collection)
    for i in range(length):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
                yield
        collection[least], collection[i] = (collection[i], collection[least])

def shell_sort(collection):
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
                yield
            collection[j] = temp
            i += 1

def is_sorted(collection):
    if len(collection) < 2:
        return True
    for i in range(len(collection) - 1):
        if collection[i] > collection[i + 1]:
            return False
    return True

def bogo_sort(collection):
    while not is_sorted(collection):
        random.shuffle(collection)
        yield
    return collection

def gnome_sort(collection):
    """
    Pure implementation of the gnome sort algorithm in Python.
    """
    if len(collection) <= 1:
        return collection
        
    i = 1
    
    while i < len(collection):
        if collection[i-1] <= collection[i]:
            i += 1
        else:
            collection[i-1], collection[i] = collection[i], collection[i-1]
            yield
            i -= 1
            if (i == 0):
                i = 1
                
def insertion_sort(collection):
    """Pure implementation of the insertion sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertion_sort([])
    []
    >>> insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    for index in range(1, len(collection)):
        while 0 < index and collection[index] < collection[index - 1]:
            collection[index], collection[index - 1] = collection[index - 1], collection[index]
            yield
            index -= 1
            
def heapify(collection, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and collection[left_index] > collection[largest]:
        largest = left_index
    if right_index < heap_size and collection[right_index] > collection[largest]:
        largest = right_index
    if largest != index:
        collection[largest], collection[index] = collection[index], collection[largest]
        heapify(collection, largest, heap_size)

def heap_sort(collection):
    n = len(collection)
    for i in range(n // 2 - 1, -1, -1):
        yield
        heapify(collection, i, n)
    for i in range(n - 1, 0, -1):
        collection[0], collection[i] = collection[i], collection[0]
        yield
        heapify(collection, 0, i)
        yield

def sub_partition(array, start, end, idx_pivot):
    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    yield
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            yield
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    yield
    return i - 1

def quick_sort(array, start=0, end=None, depth = 0):
    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    idx_pivot = random.randint(start, end)
    i = yield from sub_partition(array, start, end, idx_pivot)
    
    yield from quick_sort(array, start, i - 1, depth+1)
    yield from quick_sort(array, i + 1, end, depth+1)
    
    