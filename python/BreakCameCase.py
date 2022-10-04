def solution(s):
    newstr = ""
    for i in s:
        if i.islower():
            newstr += i
        else:
            newstr += f" {i}"
    return newstr


# test.assert_equals(solution("helloWorld"), "hello World")
# test.assert_equals(solution("camelCase"), "camel Case")
# test.assert_equals(solution("breakCamelCase"), "break Camel Case")
