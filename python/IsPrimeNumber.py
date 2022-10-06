def is_prime(num):
    if num <= 1:
        return False
    for i in range(num):
        if i == num or i == 1 or i == 0:
            continue
        elif num % i == 0:
            return False
    return True


is_prime(1)
is_prime(2)
is_prime(73)
is_prime(75)
is_prime(-1)
