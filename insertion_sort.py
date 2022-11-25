def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

unsorted_list = [1,2,3,6,7,78,4,2,43,456,78,3,2,4,6,87,8,232,4,5,76,4,2,4]

print(insertion_sort(unsorted_list))