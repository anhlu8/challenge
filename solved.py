array = [4,1,3,4,2]


def shuffle(my_list):
    new_array=[my_list[0]]
    for x in range(len(my_list)-1):
        new_array.append(my_list[new_array[-1]])
    return len(set(new_array))



print(shuffle(array))


# I changed my answers to this question multiple times. It took me more than half a day to really understand the question. 
# I think what had made me confused was this sentence: "​It then uses that value as the index for the next value to return, and so on​."
# I think I would have understood the problem better if that sentence was written: "It then uses that value as the index of the next value to return, and so on​."

# Part b:
# I haven't worked a lot with big O, but from my research I think using only a constant amount of additional memory would not work for part a. 
# I think since the input is a list of size N, which means the total Space Complexity would be equal to N plus constant space in other words using only a constant amount of additional memory wouldn't work.

