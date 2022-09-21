# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


def find_outlier(arr):
    # create a state varaible
    # check array state
    #   loop through array
    #       keep a count of number of odd and evenr items in array
    #       set the state  with respect to the greater count
    # if state is  even else state is odd
    # look for up opposing state number
    #   loop through array
    #       check for the item that matchs state
    #  print (osn this array is (state))
    e_count = 0
    o_count = 0
    for i in arr:
        if i % 2 == 0:
            e_count += 1
        else:
            o_count += 1
    if e_count > o_count:
        for i in arr:
            if i % 2 != 0:
                print("{i} the only odd number")
    else:
        for i in arr:
            if i % 2 == 0:
                print(f"{i} the only even number")


find_outlier([160, 3, 1719, 19, 11, 13, -21])
