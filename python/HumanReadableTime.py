# Write a function, which takes a non-negative
# integer (seconds) as input and returns the
# time in a human-readable format (HH:MM:SS).

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59

# The maximum time never exceeds 359999 (99:59:59)


# test.assert_equals(make_readable(0), "00:00:00")
# test.assert_equals(make_readable(5), "00:00:05")
# test.assert_equals(make_readable(60), "00:01:00")
# test.assert_equals(make_readable(86399), "23:59:59")
# test.assert_equals(make_readable(359999), "99:59:59")
import math


def formatNum(n):
    if n == 0:
        return "00"
    elif n < 10:
        return f"0{n}"
    else:
        return str(n)


def formatTime(li):
    fArr = []
    for i in li:
        fArr.append(formatNum(i))
    return f"{fArr[0]}:{fArr[1]}:{fArr[2]}"


def humanReadableTime(sec):
    min = 0
    hr = 0
    if sec > 59:
        min = math.floor(sec / 60)
        sec = sec % 60
        if min > 59:
            hr = math.floor(min / 60)
            min = min % 60
            return formatTime([hr, min, sec])
        else:
            return formatTime([hr, min, sec])
    else:
        return formatTime([hr, min, sec])


humanReadableTime(0)
humanReadableTime(5)
humanReadableTime(60)
humanReadableTime(86399)
humanReadableTime(359999)
