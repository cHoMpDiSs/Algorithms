def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

my_list = [1,3,5,7,54,23,21,5,7,9,9,7543,34,56,65,43,2312,2365,8,789,6,54,3423,3234]

print(bubblesort(my_list))