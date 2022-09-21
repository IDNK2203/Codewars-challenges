# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []


def in_array(array1, array2):
    sorts = []
    for i in array1:
        for j in array2:
            if i in j:
                sorts.append(i)
    sorts.sort()
    print(list(dict.fromkeys(sorts)))


a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
in_array(a1, a2)
