def remove_number(int_list):
    position=3-1
    index=0
    len_list=(len(numbers))
    while len_list>=0:
        index=(position+index) % len_list
        print(numbers.pop(index))
        len_list-=1


numbers=[1,2,3,4,5,7]
remove_number(numbers)
