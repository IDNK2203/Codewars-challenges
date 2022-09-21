# def digital_root(n):
#     store = n
#     while len(str(store)) > 1:
#         strN = str(n)
#         for i in strN:
#             i = int(i)
#             store = store + i
#     print(store)


def digital_root(n):
    str_n = str(n)
    while len(str_n) > 1:
        n = sum(int(x) for x in str_n)
        str_n = str(n)
    print(n)


digital_root(88)


def get_middle(s):
    mid = len(s) / 2
    if len(s) % 2 == 0:
        print(s[int(mid) - 1 : int(mid) + 1])
    else:
        print(s[int(mid)])


get_middle("test")
get_middle("testing")
