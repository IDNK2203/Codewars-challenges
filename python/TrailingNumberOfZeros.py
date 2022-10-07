# soltion timedout
def zeros(n):
    _f = 1
    for i in range(n + 1):
        if i == 0 or i == 1:
            continue
        _f = _f * i
    __s = str(_f)[::-1]
    count = 0
    for i in __s:
        if int(i) != 0:
            break
        count += 1
    print(count)


zeros(0)
# , 0,
zeros(6)
# , 1,
zeros(30)
# , 7
