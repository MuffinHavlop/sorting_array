def sorting_system(array):
    for i in range(1, len(array)):
        while array[i - 1] > array[i] and i > 0:
            array[i - 1], array[i] = array[i], array[ i - 1]
            i -= 1
    

array = [3, 5, 6, 7, 2, 1, 9, 0, 16, 11, 12, 14]
sorting_system(array)
print(array)