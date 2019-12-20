array = [4,1,3,4,2]
# array = [1,2,0]


def my_count(my_list):
    my_new_list = [my_list[0]]
    for x, el in enumerate(my_list):
        my_new_list.append(my_list[my_new_list[x]])
    return len(set(my_new_list))

print(my_count(array))
        




