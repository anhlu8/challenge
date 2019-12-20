# Part a
import sys

lines = []

def remove_duplicates_in_a_file(file):
    array = []
    for line in file:
        if line not in array:
            array.append(line)
    return array
    
def count_line(file):
    new_file = remove_duplicates_in_a_file(file)
    for line in new_file: 
        newline = line.strip()
        lines.append(newline)
    file.close()

count_line(open(sys.argv[1]))
count_line(open(sys.argv[2]))
    
common_lines=[i for i in lines if lines.count(i) > 1]
print(len(common_lines))

# To run this program: python solved2.py text1.txt text2.txt

##########################
##########################
# Part 2b

# I would not change my approach if there are still only 2 files. If there are more than 2 files, I would create a new function to loop through the number of argv and invoke function count_line within my new function

# import sys

# lines = []

# def remove_duplicates_in_a_file(file):
#     array = []
#     for line in file:
#         if line not in array:
#             array.append(line)
#     return array
    
# def count_line(file):
#     new_file = remove_duplicates_in_a_file(file)
#     for line in new_file: 
#         newline = line.strip()
#         lines.append(newline)
#     file.close()

# argv_num = len(sys.argv)

# def new_func(num):
#     new_num = num - 1
#     for i in range(new_num):
#         count_line(open(sys.argv[i+1]))

# new_func(argv_num)
    
# common_lines=[i for i in lines if lines.count(i) > 1]
# print(len(common_lines))