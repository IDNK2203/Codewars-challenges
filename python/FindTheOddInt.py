# solution Timedout


def find_it(seq):
    histo = {}
    for i in seq:
        histo[i] = histo.get(i, 0) + 1
    for k, v in histo.items():
        if v % 2 != 0:
            print(k)


find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
# should return 5 (because it appears 3 times)")
find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
# should return -1 (because it appears 1 time)")
find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
# should return 5 (because it appears 3 times)")
find_it([10])
# should return 10 (because it appears 1 time)")
find_it([10, 10, 10])
# should return 10 (because it appears 3 times)")
find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
# should return 10 (because it appears 1 time)")
find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10])
# should return 1 (because it appears 1 time)")
