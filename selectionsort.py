def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

    return arr


my_list = [1,3,5,7,54,23,21,5,7,9,9,7543,34,56,65,43,2312,2365,8,789,6,54,3423,3234]

print(selection_sort(my_list))
        















my_list = [1,3,5,7,54,23,21,5,7,9,9,7543,34,56,65,43,2312,2365,8,789,6,54,3423,3234]